# 🎬 ASKTube: Conversation with YouTube!

A Streamlit app for interactive conversations with YouTube videos, powered by AI-generated answers from video transcripts.

![Banner](./img/app_banner.png)

## 🚀 Features

- 🎤 Automatically transcribes YouTube videos (using Whisper).
- 🤖 Answers your questions using RAG (Retrieval Augmented Generation) based on video content.
- 🔎 Search for videos on YouTube by keyword.
- 🌐 Gemini Pro and OpenAI integration.
- 🖥️ Modern and user-friendly interface.

## 🛠️ Installation

1. **Clone the repository:**

   ```sh
   git clone <repo-url>
   cd talk-to-youtube
   ```

2. **Install required Python packages:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Add your API keys to a `.env` file:**

   ```env
   openai_apikey=YOUR_OPENAI_API_KEY
   google_apikey=YOUR_GOOGLE_API_KEY
   ```

## ▶️ Usage

```sh
streamlit run app.py
```

- Enter a YouTube video link in the **URL** tab, type your question, and click "Ask".
- The app will download the audio, transcribe it, and answer your question using the video content.
- You will also see relevant reference texts and sources alongside the answer.

## 📁 File Structure

- `app.py`: Streamlit interface and main app flow.
- `videohelper.py`: Video transcription and YouTube search functions.
- `raghelper.py`: RAG and LLM (Gemini Pro) answer generation.
- `youtubevideo.py`: YouTube video object definition.
- `requirements.txt`: Required Python packages.

## 📋 Requirements

- Python 3.8+
- OpenAI and Google API keys

## 🤝 Contributing

Feel free to open a pull request or create an issue to contribute.
