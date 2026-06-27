import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import requests
import joblib
from openai import OpenAI
from dotenv import load_dotenv
import os

# Fetching our OpenAI Api
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Importing JobLib model
df = joblib.load("embeddings.joblib")


# Function to create the embeddings and here we are processing in batches so that it can be memory efficient
def create_embeddings(text_list, batch_size=300):
    all_embeddings = []
    for start in range(0, len(text_list), batch_size):
        end = start + batch_size
        batch = text_list[start:end]

        r = requests.post(
            "http://localhost:11434/api/embed", json={"model": "bge-m3", "input": batch}
        )

        response = r.json()

        all_embeddings.extend(response["embeddings"])
    return all_embeddings


# Using OpenAI api to generate the response by feeding prompt to GPT model
def inferance_OpenAI(prompt):
    print("Thinking....")
    response = client.responses.create(
        model="gpt-5", input=prompt, text={"verbosity": "low"}
    )

    return response.output_text


# Taking user query and creating embeddings from it
def ask_question(incoming_query):

    question_embeddings = create_embeddings(incoming_query, 300)[0]

    # Finding the similarity between question and df embeddings
    similarities = cosine_similarity(
        np.vstack(df["embedding"].values), [question_embeddings]
    ).flatten()
    best_similarity = similarities.max()
    SIMILARITY_THRESHOLD = 0.55

    top_results = 5
    max_index = similarities.argsort()[::-1][0:top_results]
    new_df = df.loc[max_index]

    # Best matching chunk
    best_match = new_df.iloc[0]

    video_title = best_match["title"]
    video_number = best_match["number"]
    start_time = best_match["Start"]
    end_time = best_match["End"]
    video_text = best_match["text"]

    # This is the prompt which we will feed to LLM model and then it will generate the response
    prompt = f"""
        You are an AI assistant for a Web Development course.

        Below are the most relevant subtitle chunks retrieved from the course.

        {new_df[['title','number','Start','End','text']].to_string(index=False)}

        User Question:
        {incoming_query}

        Answer ONLY using the provided context.

        Explain the concept in simple language.
        """

    output = inferance_OpenAI(prompt)

    if best_similarity < SIMILARITY_THRESHOLD:
        return {
            "video_title": "",
            "video_number": "",
            "start_time": "",
            "end_time": "",
            "answer": "I couldn't find this topic in the uploaded course videos."
        }
    return {
        "video_title": video_title,
        "video_number": video_number,
        "start_time": start_time,
        "end_time": end_time,
        "answer": output,
    }


# resp = ask_question(input("Enter the query: "))
# print(resp)

# Writing the prompt in a .txt files
# with open("prompt.txt", "w") as f:
#     f.write(prompt)
