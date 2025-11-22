from flask import Flask, request, jsonify, send_from_directory
from faq_data import FAQ_DATA, model
from smalltalk import SMALLTALK
import numpy as np

app = Flask(__name__, static_folder="static")

def find_semantic_answer(question):
    q = question.lower().strip()

    # 1. Smalltalk check first
    for key in SMALLTALK:
        if key in q:
            return SMALLTALK[key]

    # 2. Semantic search
    question_emb = model.encode(question)
    best_score = -1
    best_answer = None

    for item in FAQ_DATA:
        faq_emb = np.array(item["embedding"])
        score = np.dot(question_emb, faq_emb) / (
            np.linalg.norm(question_emb) * np.linalg.norm(faq_emb)
        )

        if score > best_score:
            best_score = score
            best_answer = item["a"]

    # Lowered threshold for better matching
    if best_score > 0.40:
        return best_answer

    return "I'm not sure about that, but I can help with orders, returns, payments, or general queries!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    answer = find_semantic_answer(question)
    return jsonify({"answer": answer})

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True)
