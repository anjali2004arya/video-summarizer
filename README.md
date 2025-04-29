# 🧠 AI Agent: Video Transcription & Summarization

This project automatically **extracts audio from a video**, transcribes it using **OpenAI Whisper**, and then **summarizes the transcript** using a Hugging Face transformer model like `facebook/bart-large-cnn`.

---

## 📁 Project Structure

```
AI Agent Transcribing and Summarizing/
├── main.py                 # Orchestrates video-to-summary pipeline
├── transcriber.py          # Handles audio extraction and Whisper transcription
├── summarizer.py           # Uses a transformer model to summarize text
├── utils.py                # Contains chunking logic for large transcripts
├── example_video.mp4       # Sample video file to test the pipeline
├── requirements.txt        # Dependencies
└── README.md               # This file
```

---

## 🚀 Features

- 🎥 Extracts audio from any video
- 📝 Transcribes speech to text using OpenAI Whisper
- ✂️ Automatically chunks long transcripts
- 📄 Summarizes text using Hugging Face transformer models
- ⚙️ Supports multiple Whisper sizes (`tiny`, `base`, `small`, `medium`, `large`)

---

## 🔧 Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/video-audio-summarizer.git
cd video-audio-summarizer
```

### 2. Create and activate a conda environment

```bash
conda create -n video_audio_summarizer python=3.9
conda activate video_audio_summarizer
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, you can install manually:

```bash
pip install openai-whisper torch transformers ffmpeg-python
```

---

## ▶️ How to Run

Run the main script with a video file:

```bash
python main.py
```

### You can modify the parameters in `main.py`:

- `model_size`: Whisper model size (`tiny`, `base`, `small`, `medium`, `large`)
- `summarizer_model_name`: Hugging Face summarization model (`facebook/bart-large-cnn`, etc.)
- `use_chunking`: Set `True` to enable chunk-wise summarization for long transcripts

---

## 💡 Optional Enhancements (TODO)

- Build a Streamlit UI for uploading videos and viewing summaries
- Add support for more summarizer models
- Handle multi-language audio with Whisper's language detection
- Display video timeline with summary mapping

---

## 🛠 Example Requirements

```txt
openai-whisper
torch
transformers
ffmpeg-python
```

Create it using:

```bash
pip freeze > requirements.txt
```

---
