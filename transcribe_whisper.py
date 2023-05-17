import whisper
import os

model = whisper.load_model("base")

thisdir = os.getcwd()

for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith(".mp3"):
            print('Procesando '+ file)
            audio = whisper.load_audio(file)

            options = {
                "language": "es",
                "task": "transcribe",
                "fp16": False
            }

            result = whisper.transcribe(model, audio, **options)
            print(result["text"])

            with open(file.split(".")[0]+'.txt', 'w', encoding="utf-8") as f:
                f.write(result["text"])