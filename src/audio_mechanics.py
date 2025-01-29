import os
from io import BytesIO
from google.cloud import texttospeech
from pydub import AudioSegment
from pydub.playback import play

def speak_text_in_memory(text: str, language_code="en-US", gender="MALE"):
    """
    Generates TTS audio from 'text' using Google Cloud TTS, 
    then plays it immediately from memory (no file saved).
    """
    client = texttospeech.TextToSpeechClient()

    # ssml_text = f"<speak intro start>{text}"
    synthesis_input = texttospeech.SynthesisInput(text=text)

    if gender.upper() == "MALE":
        ssml_gender = texttospeech.SsmlVoiceGender.MALE
    elif gender.upper() == "FEMALE":
        ssml_gender = texttospeech.SsmlVoiceGender.FEMALE
    else:
        ssml_gender = texttospeech.SsmlVoiceGender.NEUTRAL

    voice = texttospeech.VoiceSelectionParams(
        language_code = language_code,
        ssml_gender = ssml_gender
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding = texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    mp3_data = response.audio_content

    audio_segment = AudioSegment.from_file(BytesIO(mp3_data), format="mp3")

    play(audio_segment)
