# 🎥 AI Video Course Assistant

A Retrieval-Augmented Generation (RAG) application that enables users to search course videos using natural language and instantly find the exact video and timestamp where a topic is explained.

Instead of manually watching hours of course content, users can ask questions such as:

«"Where is Cosine Similarity explained?"»

The application retrieves the most relevant transcript chunks using semantic search and generates a concise answer using OpenAI GPT-5, along with the corresponding video and timestamp.

---

## 🚀 Features

- 🎬 Convert course videos (MP4) into audio using FFmpeg
- 🎙️ Generate transcripts using OpenAI Whisper
- 📝 Store transcripts in JSON format
- 🧠 Generate embeddings using BGE-M3 (Ollama)
- 🔍 Retrieve relevant transcript chunks using Cosine Similarity
- 🤖 Generate responses using OpenAI GPT-5
- 🌐 ChatGPT-style web interface built with Flask
- 📹 Display the most relevant video
- ⏰ Display the exact timestamp for the requested topic
- ❌ Gracefully handle questions unrelated to the uploaded course

---

## 🏗️ System Architecture

                User Query
                     │
                     ▼
          Flask Web Application
                     │
                     ▼
             Create Query Embedding
                     │
                     ▼
          Cosine Similarity Search
                     │
                     ▼
         Retrieve Top Relevant Chunks
                     │
                     ▼
        Prompt Engineering + GPT-5
                     │
                     ▼
          Structured AI Response
                     │
                     ▼
      Video + Timestamp + Explanation

---

## 🛠️ Tech Stack

Backend

- Python
- Flask

AI & Machine Learning

- OpenAI GPT-5
- OpenAI Whisper
- Ollama
- BGE-M3 Embeddings
- Cosine Similarity
- Scikit-Learn
- NumPy
- Pandas

Frontend

- HTML
- CSS
- JavaScript

---

## ⚙️ Workflow

1. Convert MP4 videos to MP3 using FFmpeg.
2. Generate transcripts using Whisper.
3. Store transcript chunks as JSON.
4. Generate embeddings using BGE-M3.
5. Store embeddings in a Joblib file.
6. Accept user questions through the web interface.
7. Generate query embeddings.
8. Retrieve the most relevant transcript chunks using Cosine Similarity.
9. Pass the retrieved context to GPT-5.
10. Display:

- Relevant Video
- Timestamp
- AI-generated explanation

---

## 📸 Screenshots

![Home Page](screenshots/home.png)

---

![Example Response](screenshots/answer.png)

---

## 🧠 Example

User Question

Where are HTML headings explained?

Response

📹 Video:
HTML Tutorial

🎬 Video Number:
8

⏰ Timestamp:
18:42

💬 Explanation

You’ll find it in “Image, Lists, and Tables in HTML” (Lesson 5): - 421.68–426.68: Using the table tag and the tr tag. - 541.68–546.68: Understanding it’s a table in HTML. - 571.68–586.68: What a table looks like; practice making tables/projects. - 796.68–801.68: Whole table with head content and foot content. Simple idea: A table is built with a table tag. Inside it, you add row tags (tr). Tables can include head content and foot content.
---

## 📌 Future Improvements

- 🎥 Direct video playback from the application
- ⏱️ Clickable timestamps
- 📂 Support multiple courses
- 👤 User authentication
- 💬 Conversation history
- 📱 Improved responsive UI
- ☁️ Cloud deployment
- 🔎 Hybrid Search (Keyword + Semantic Search)

---

## 💡 Learning Outcomes

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG
