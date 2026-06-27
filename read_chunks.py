import requests
import os
import json
import pandas as pd
import joblib

# Here we will create the embeddings for the text we have in chunks which will represent the text in vector in high dimension and then we can use the cosine similarity to check the similaity between the query and the text and return the response.
def create_embeddings(text_list, batch_size = 400):
    all_embeddings = []
    for start in range(0, len(text_list), batch_size):
        end = start + batch_size
        batch = text_list[start:end]

        r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": batch
        })

        response = r.json()
        
        all_embeddings.extend(response["embeddings"])
    return all_embeddings

# a = create_embeddings(["Always be calm", "Peace is the goal"])
# print(a)

jsons = os.listdir("new_jsons")

my_dict = []
chunk_id = 0

for json_file in jsons:
    with open(f"new_jsons/{json_file}") as f:
        content = json.load(f)
    print(f"Creating embeddings for {json_file}")
    embeddings_list = create_embeddings([c['text'] for c in content['chunks']], batch_size = 400)

    for i, chunk in enumerate(content["chunks"]):
        chunk["chunk_id"] = chunk_id
        chunk["embedding"] = embeddings_list[i]
        chunk_id += 1
        my_dict.append(chunk)  

        # print(chunk) 
        # print("/n")    
    # break

df = pd.DataFrame.from_records(my_dict)

# Saving the DATAFRAME
joblib.dump(df, "embeddings.joblib")





