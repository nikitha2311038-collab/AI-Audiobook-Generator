# AI-Audiobook-Generator
# AI Audiobook Generator

## Overview
AI Audiobook Generator is a Python-based application that converts text documents into natural-sounding audiobooks using Artificial Intelligence and Natural Language Processing (NLP). The application extracts text from input files, preprocesses and enriches the content, and generates high-quality speech output.

## Features
- Extracts text from PDF and text documents.
- Cleans and preprocesses extracted content.
- Enriches text using AI for improved readability.
- Converts processed text into speech.
- Generates audiobook audio in MP3 format.
- Modular and scalable Python architecture.

## Technologies Used
- Python
- Natural Language Processing (NLP)
- Google Gemini API
- ChromaDB
- Retrieval-Augmented Generation (RAG)
- Text-to-Speech (TTS)
- FFmpeg
- Git & GitHub

## Project Structure

```
AI-Audiobook-Generator/
│
├── audio_output/
├── input_files/
├── rag/
├── extractor.py
├── enricher.py
├── list_models.py
├── main.py
├── requirements.txt
├── transcribe.py
├── tts.py
├── tts_generator.py
└── README.md
```

## Installation

1. Clone the repository.

```bash
git clone https://github.com/yourusername/AI-Audiobook-Generator.git
```

2. Navigate to the project folder.

```bash
cd AI-Audiobook-Generator
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

4. Configure your API key in a `.env` file.

Example:

```
GEMINI_API_KEY=YOUR_API_KEY
```

## Run the Project

Execute the following command:

```bash
python main.py
```

## Output

The application:
- Reads the input document.
- Extracts and preprocesses text.
- Enhances content using AI.
- Generates speech from the processed text.
- Saves the audiobook as an MP3 file.

## Skills Demonstrated

- Python Programming
- Object-Oriented Programming
- File Handling
- Natural Language Processing
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- API Integration
- Error Handling
- AI Application Development

## Future Enhancements

- Support for multiple languages.
- Voice selection options.
- Web-based interface using Streamlit.
- Real-time audiobook generation.
- Cloud deployment.

## Author

**Nikitha M**

B.Tech Artificial Intelligence and Data Science

Sri Ramakrishna Engineering College
