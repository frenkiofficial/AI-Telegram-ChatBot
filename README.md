# 🔥 AI Telegram Chatbot (OpenAI/Gemini) 🔥

A simple yet powerful Telegram bot that allows users to chat directly with an AI (powered by OpenAI or Google Gemini API) within their Telegram application. This repository provides the basic implementation.


## ✅ Basic Features (Included in this Repository)

*   **AI-Powered Responses:** Leverages OpenAI (e.g., GPT-3.5-Turbo, GPT-4) or Google Gemini (e.g., Gemini Pro) API to answer user messages.
*   **Direct Chat:** Simply send a message to the bot, and the AI will reply.
*   **Handles Short & Long Messages:** Capable of engaging in brief Q&A or more extended discussions.
*   **/start Command:** Provides users with a welcome message and basic instructions.
*   **Easy API Key Configuration:** Uses a `.env` file for securely managing API keys and selecting the AI provider (OpenAI/Gemini).
*   **Flexible AI Backend:** Choose between OpenAI or Gemini by changing a single variable in the `.env` file.

##  Prerequisites

Before you begin, ensure you have the following:

1.  **Python:** Version 3.8 or newer installed.
2.  **Telegram Account:** You need a Telegram account to interact with the bot.
3.  **Telegram Bot Token:** Create a bot using [BotFather](https://t.me/BotFather) on Telegram to get your unique token.
4.  **AI Provider API Key:**
    *   **OpenAI:** An API key from [OpenAI Platform](https://platform.openai.com/).
    *   **Google Gemini:** An API key from [Google AI Studio](https://aistudio.google.com/app/apikey) or Google Cloud.
5.  **Git** (Optional but recommended): For cloning the repository easily.

## ⚙️ Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/frenkiofficial/AI-Telegram-ChatBot.git
    cd AI-Telegram-ChatBot # Navigate into the cloned directory
    ```
    *(Alternatively, download the code as a ZIP file and extract it.)*

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    # If you plan to use Gemini and didn't uncomment it in requirements.txt:
    # pip install google-generativeai
    ```

## 🔑 Configuration (.env File)

1.  **Navigate** into the `AI-Telegram-ChatBot` directory if you haven't already.
2.  **Create a `.env` file** in this directory.
3.  **Copy and paste** the following content into the `.env` file:

    ```env
    # --- Telegram Configuration ---
    TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN_HERE"

    # --- AI Provider Configuration ---
    # Choose ONE provider: "openai" or "gemini"
    AI_PROVIDER="openai"

    # --- OpenAI Configuration (if AI_PROVIDER="openai") ---
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY_HERE"
    # Optional: Specify OpenAI model (default: gpt-3.5-turbo)
    OPENAI_MODEL="gpt-3.5-turbo"

    # --- Google Gemini Configuration (if AI_PROVIDER="gemini") ---
    # Uncomment and fill if using Gemini
    # GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
    # Optional: Specify Gemini model (default: gemini-pro)
    # GEMINI_MODEL="gemini-pro"
    ```

4.  **Replace the placeholder values:**
    *   `YOUR_TELEGRAM_BOT_TOKEN_HERE` with your actual bot token from BotFather.
    *   Set `AI_PROVIDER` to either `"openai"` or `"gemini"`.
    *   If using OpenAI: Fill `YOUR_OPENAI_API_KEY_HERE` with your OpenAI key.
    *   If using Gemini: Fill `YOUR_GOOGLE_API_KEY_HERE` with your Google API key.
    *   Adjust `OPENAI_MODEL` or `GEMINI_MODEL` if you want to use a different model version (optional).

5.  **Important Security Note:** Ensure `.env` is listed in your `.gitignore` file to prevent accidentally committing your secret keys! If a `.gitignore` file doesn't exist, create one and add `.env` to it.

## ▶️ Running the Bot

1.  Make sure your virtual environment is activated (if you created one).
2.  Ensure you are in the `AI-Telegram-ChatBot` directory in your terminal.
3.  Run the bot script:
    ```bash
    python bot.py
    ```
4.  The bot should now be running and connected to Telegram. You'll see log messages in your terminal confirming it started.

## 💬 How to Use the Bot

1.  Open Telegram and search for the bot username you created with BotFather.
2.  Start a chat with your bot.
3.  Send the `/start` command to see the welcome message.
4.  Send any text message to the bot. It will process your message using the configured AI (OpenAI or Gemini) and send back the response.

---

## 🚀 Advanced Features & Custom Development

This repository provides a foundational AI chatbot. If you need more advanced capabilities or custom modifications, I offer development services to enhance this bot.

**Potential Advanced Features:**

*   🔹 **Conversational Memory:** Enable the AI to remember previous parts of the conversation within a session for better context.
*   🖼️ **Image Generation:** Integrate DALL-E (via OpenAI) or Gemini Vision capabilities to generate images based on text prompts.
*   📊 **Usage Limits & Token Control:** Implement mechanisms to monitor and limit API usage per user or globally to manage costs.
*   📝 **Google Sheets Logging:** Automatically log conversation history or important interactions to a Google Sheet for analysis or record-keeping.
*   🎭 **AI Personalization (Custom Prompts):** Configure the AI's personality, tone (formal, casual, funny), or role using custom system prompts.
*   ⚙️ **And more:** Database integration, user management, custom commands, etc.

**Interested in adding these features or need other custom Telegram bot development?**

Feel free to reach out to me through any of the following platforms:

*   **GitHub:** [frenkiofficial](https://github.com/frenkiofficial)
*   **Hugging Face:** [frenkiofficial](https://huggingface.co/frenkiofficial)
*   **Telegram:** [@FrenkiOfficial](https://t.me/FrenkiOfficial)
*   **Twitter / X:** [@officialfrenki](https://twitter.com/officialfrenki)
*   **Fiverr:** [frenkimusic](https://www.fiverr.com/frenkimusic/)

Let's discuss how we can build the perfect AI bot for your needs!

---

*(Optional: Add a License section here, e.g., MIT License)*
