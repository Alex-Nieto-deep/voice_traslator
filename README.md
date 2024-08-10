# voice_traslator

Este proyecto es un traductor de voz que utiliza IA para transcribir y traducir audios en español a múltiples idiomas, incluyendo inglés, italiano, francés y portugués. El proyecto también genera audios traducidos usando la API de ElevenLabs.

## Requisitos

Asegúrate de tener instalado Python 3.9 o superior. Luego, instala las dependencias necesarias utilizando el archivo `requirements.txt`:

pip install -r requirements.txt

Crea un archivo .env en el directorio raíz del proyecto y añade tu clave API de ElevenLabs:
ELEVENLABS_API_KEY=your_elevenlabs_api_key

Asegúrate de que ffmpeg esté instalado en tu sistema para procesar archivos de audio.
Instalación de ffmpeg en Linux:
sudo apt-get update
sudo apt-get install ffmpeg

## Uso

python -u app.py
