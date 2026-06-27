from flask import Flask, render_template, request, jsonify
from rag_engine import ask_question

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        question = data.get("question")

        if not question:
            return jsonify(
                {
                    "answer": "Please enter a question."
                }
            )

        result = ask_question(question)

        return jsonify(result)

    except Exception as e:

        return jsonify(
            {
                "answer": str(e)
            }
        )


if __name__ == "__main__":
    app.run(debug=True)