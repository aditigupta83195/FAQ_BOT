<<<<<<< HEAD

=======
CSE Project- FAQ Chatbot
OVERVEW
This project implements a semantic FAQ chatbot capable of understanding user queries by meaning rather than exact wording. The system uses sentence embeddings to identify the closest FAQ entry and returns the most relevant answer. It includes a responsive web interface, a Python Flask backend, and a lightweight transformer model for efficient semantic similarity checks.

FEATURES

1.Semantic Search: Matches meaningfully similar questions using sentence embeddings.

2.Smalltalk Handling: Responds to common greetings and brief conversational messages.

3.Interactive Chat UI: Smooth message display with typing indicators.

4.Fast & Lightweight: Works without GPU and responds quickly.

5.Modular Codebase: Clear separation of backend, embeddings, FAQ data, and frontend logic.

6.Fallback System: Displays a friendly message when no FAQ match is found.

TECHNOLOGIES / TOOLS USED

Backend:-

Python 3.x

Flask

Sentence Transformers

NumPy

Frontend:-

HTML

CSS

JavaScript (Fetch API)

Development Tools:-

VS Code

Browser DevTools

INSTALLATION AND SETUP
1.Clone the Repository
git clone <your-repo-url>
cd <project-folder>
2.Install Required Python Packages
pip install flask sentence-transformers numpy
3.Project Structure
project/
│
├── app.py
├── faq_data.py
├── smalltalk.py
│
└── static/
    ├── index.html
    ├── style.css
    └── script.js
4.Run the Flask Server
python app.py
5.Open the Application
Visit the following URL in your browser:
http://127.0.0.1:5000/

TESTING INSTRUCTIONS
✔ Test FAQ Matching

Try questions such as:

“Refund timeline?”

“How long does a refund take?”

“When will I receive my refund?”

All should give the same answer.

✔ Test Smalltalk

Examples:

“Hi”

“Thank you”

“How are you?”

✔ Test Unknown Questions

Try:

“How to cook pasta?”

“Explain quantum theory.”

These should trigger the fallback response.

✔ Test Backend Connectivity

Open browser → Inspect → Network → Verify /ask API calls.

SCREENSHOTS

<img width="1917" height="906" alt="chatb" src="https://github.com/user-attachments/assets/cc0f2465-c287-4bfc-99ec-382a694a05d0" />

<img width="1912" height="303" alt="chatb1" src="https://github.com/user-attachments/assets/0161248d-c143-47ae-9c36-80e09f09270b" />

<img width="1908" height="253" alt="chatb2" src="https://github.com/user-attachments/assets/56bd5e1b-c87f-4bed-9000-dbd3fb8ef18a" />

<img width="1902" height="261" alt="chatb3" src="https://github.com/user-attachments/assets/ec9ca0cc-8b7d-47b1-ae27-40957cceaf10" />

<img width="1916" height="332" alt="chatb4" src="https://github.com/user-attachments/assets/f9df7c76-ffa1-42bc-b53b-bd7416e76b9c" />
>>>>>>> cd1afe31a41d2fe79748fecdd65a5fa151cc8e45
