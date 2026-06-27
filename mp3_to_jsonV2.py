import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Fetching our OpenAI Api
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
audios = os.listdir("audios")

for audio in audios:

    if "_" in audio:
        number = audio.split("_")[0]
        title = audio.split("_")[1][:-4]
        print(number, title)

        with open(f"audios/{audio}", "rb") as audio_file:
            translation = client.audio.translations.create(
                model="whisper-1",  # or "gpt-4o-audio"
                file=audio_file,
                response_format="verbose_json",
            )

        translation_data = translation.model_dump()

        segments = translation_data["segments"]

        chunks = []

        CHUNK_SIZE = 5  # Merge every 5 whisper segments

        for i in range(0, len(segments), CHUNK_SIZE):

            group = segments[i : i + CHUNK_SIZE]

            combined_text = " ".join(segment["text"].strip() for segment in group)

            chunks.append(
                    {
                "number": number,
                "title": title,
                "Start": group[0]["start"],
                "End": group[-1]["end"],
                "text": combined_text,
             }
                    )
        chunks_metadata = {"chunks": chunks, "text": translation_data["text"]}
        
        with open(f"new_jsons/{audio}.json", "w", encoding="utf-8") as f:
            json.dump(chunks_metadata, f, indent=4, ensure_ascii=False)

print("Done!")
