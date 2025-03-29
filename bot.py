import logging
import os
from dotenv import load_dotenv
from telegram import Update, ChatAction
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# --- AI Integration ---
# Import necessary AI libraries based on chosen provider
load_dotenv()
AI_PROVIDER = os.getenv("AI_PROVIDER", "openai").lower()

if AI_PROVIDER == "openai":
    try:
        import openai
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file.")
        openai.api_key = openai_api_key
        openai_client = openai.OpenAI(api_key=openai_api_key) # Use OpenAI() >= v1.0.0
        OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        print(f"Using AI Provider: OpenAI (Model: {OPENAI_MODEL})")
    except ImportError:
        print("OpenAI library not installed. Please run: pip install openai")
        exit()
    except ValueError as e:
        print(e)
        exit()

elif AI_PROVIDER == "gemini":
    try:
        import google.generativeai as genai
        google_api_key = os.getenv("GOOGLE_API_KEY")
        if not google_api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env file for Gemini.")
        genai.configure(api_key=google_api_key)
        GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-pro")
        gemini_model = genai.GenerativeModel(GEMINI_MODEL)
        # Optional: Configure safety settings if needed
        # safety_settings = [ ... ]
        # gemini_model = genai.GenerativeModel(GEMINI_MODEL, safety_settings=safety_settings)
        print(f"Using AI Provider: Google Gemini (Model: {GEMINI_MODEL})")
    except ImportError:
        print("Google Generative AI library not installed. Please run: pip install google-generativeai")
        exit()
    except ValueError as e:
        print(e)
        exit()
else:
    print(f"Error: Invalid AI_PROVIDER specified in .env: {AI_PROVIDER}. Choose 'openai' or 'gemini'.")
    exit()

# --- Telegram Bot Setup ---
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    print("Error: TELEGRAM_BOT_TOKEN not found in .env file.")
    exit()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Bot Command Handlers ---

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends explanation on how to use the bot."""
    user = update.effective_user
    await update.message.reply_html(
        f"Hi {user.mention_html()}!\n\n"
        f"I'm an AI chat bot powered by {AI_PROVIDER.capitalize()}.\n\n"
        f"Just send me any message, and I'll do my best to respond. "
        f"I can handle short questions or longer discussions.\n\n"
        f"Let's chat!",
    )

# --- AI Response Function ---

async def get_ai_response(user_message: str) -> str:
    """Gets response from the configured AI API."""
    logger.info(f"Sending to AI ({AI_PROVIDER}): {user_message[:50]}...") # Log first 50 chars

    try:
        if AI_PROVIDER == "openai":
            # --- OpenAI API Call ---
            response = await openai_client.chat.completions.create( # Use 'await' if using async client, otherwise remove
                model=OPENAI_MODEL,
                messages=[
                    # Optional: Add a system message for context/personality
                    # {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message},
                ],
                # Optional parameters:
                # max_tokens=150,
                # temperature=0.7,
            )
            ai_response = response.choices[0].message.content.strip()

        elif AI_PROVIDER == "gemini":
            # --- Gemini API Call ---
            # Note: Gemini's API might behave slightly differently regarding chat history.
            # For simple request-response, this works. For context, you'd need to manage history.
            response = await gemini_model.generate_content_async(user_message) # Use generate_content for sync
            # Handle potential blocks - check response.prompt_feedback
            if response.candidates:
                 # Check if parts exist and have text
                 if hasattr(response.candidates[0], 'content') and hasattr(response.candidates[0].content, 'parts') and response.candidates[0].content.parts:
                     ai_response = response.candidates[0].content.parts[0].text
                 else:
                     # Handle cases where the structure is different or content is missing
                     ai_response = "Sorry, I couldn't generate a text response from that."
                     logger.warning(f"Gemini response structure unexpected or empty: {response.candidates[0]}")

            elif response.prompt_feedback and response.prompt_feedback.block_reason:
                 ai_response = f"My response was blocked due to: {response.prompt_feedback.block_reason.name}. Please rephrase your request."
                 logger.warning(f"Gemini request blocked: {response.prompt_feedback.block_reason.name}")
            else:
                 ai_response = "Sorry, I received an empty response from the AI."
                 logger.warning("Gemini returned no candidates and no block reason.")


        logger.info(f"AI Response ({AI_PROVIDER}): {ai_response[:50]}...") # Log first 50 chars
        return ai_response

    except Exception as e:
        logger.error(f"Error calling {AI_PROVIDER.capitalize()} API: {e}", exc_info=True)
        return f"Sorry, I encountered an error trying to reach the AI ({AI_PROVIDER.capitalize()}). Please try again later."


# --- Message Handler ---

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles regular text messages and replies using AI."""
    user_message = update.message.text
    chat_id = update.effective_chat.id

    if not user_message: # Ignore empty messages
        return

    # Send "typing..." action
    await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)

    # Get AI response
    ai_response = await get_ai_response(user_message)

    # Send AI response back to user
    try:
        await update.message.reply_text(ai_response)
    except Exception as e:
        logger.error(f"Error sending message back to Telegram: {e}", exc_info=True)
        # Optionally notify the user about the send failure
        await update.message.reply_text("Sorry, I couldn't send the response back. Please try again.")


# --- Error Handler ---
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log Errors caused by Updates."""
    logger.error(f"Update {update} caused error {context.error}", exc_info=context.error)


# --- Main Function ---

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # --- Register Handlers ---
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Error handler
    application.add_error_handler(error_handler)

    # Run the bot until the user presses Ctrl-C
    logger.info("Starting bot polling...")
    application.run_polling()

if __name__ == "__main__":
    main()