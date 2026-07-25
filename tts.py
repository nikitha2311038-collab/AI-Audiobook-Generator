import pyttsx3
import os

def text_to_speech(text, output_path="output_audio.mp3", lang="en"):
    """
    Convert text to speech and save as mp3.
    Returns the path of the generated audio file.
    """
    if not text or text.strip() == "":
        raise ValueError("⚠️ No text provided for TTS.")

    # Initialize TTS engine
    engine = pyttsx3.init()

    # Set language if possible (pyttsx3 uses system voices)
    # For English, it should use default voice

    # Generate speech
    engine.save_to_file(text, output_path)
    engine.runAndWait()

    return output_path
