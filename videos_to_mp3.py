import whisper
import os
import subprocess

all_files = os.listdir("Videos")

for file in all_files:
    tutorial_number = file.split(" #")[1].split(" ")[0]
    file_name = file.split("_")[0].split(".com ")[1]

    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])
    
    
