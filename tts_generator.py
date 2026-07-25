from gtts import gTTS

def generate_audio(enriched_text, output_file):
    tts = gTTS(enriched_text)
    tts.save(output_file)
