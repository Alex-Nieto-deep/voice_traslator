import os
import gradio as gr
import whisper
from translate import Translator
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings


# Configuración .env
load_dotenv()
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')


def translator(audio_file):

    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_file, language="Spanish", fp16=False)
        transcription = result["text"]
    except Exception as e:
        raise gr.Error(
            f"Se ha producido un error transcribiendo el texto: {str(e)}")

    print(f"Texto original: {transcription}")

    try:
        en_transcription = Translator(
            from_lang="es", to_lang="en").translate(transcription)
        it_transcription = Translator(
            from_lang="es", to_lang="it").translate(transcription)
        fr_transcription = Translator(
            from_lang="es", to_lang="fr").translate(transcription)
        pt_transcription = Translator(
            from_lang="es", to_lang="pt").translate(transcription)
    except Exception as e:
        raise gr.Error(
            f"Se ha producido un error traduciendo el texto: {str(e)}")

    print(f"Texto traducido a Inglés: {en_transcription}")
    print(f"Texto traducido a Italiano: {it_transcription}")
    print(f"Texto traducido a Francés: {fr_transcription}")
    print(f"Texto traducido a Japonés: {pt_transcription}")

    en_save_file_path = text_to_speach(en_transcription, "en")
    it_save_file_path = text_to_speach(it_transcription, "it")
    fr_save_file_path = text_to_speach(fr_transcription, "fr")
    pt_save_file_path = text_to_speach(pt_transcription, "pt")

    return en_save_file_path, it_save_file_path, fr_save_file_path, pt_save_file_path


def text_to_speach(text: str, language: str) -> str:

    try:
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

        response = client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=0.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )

        save_file_path = f"audios/{language}.mp3"

        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)

    except Exception as e:
        raise gr.Error(
            f"Se ha producido un error creando el audio: {str(e)}")

    return save_file_path


app = gr.Interface(
    fn=translator,
    inputs=gr.Audio(
        sources=["microphone"],
        type="filepath",
        label="Español"
    ),
    outputs=[
        gr.Audio(label="Inglés"),
        gr.Audio(label="Italiano"),
        gr.Audio(label="Francés"),
        gr.Audio(label="Portuges")
    ],
    title="Traductor de voz",
    description="Traductor de voz con IA a varios idiomas"
)

app.launch()