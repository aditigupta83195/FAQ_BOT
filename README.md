<h1 align="center">🤖 CSE Project – Semantic FAQ Chatbot</h1>

<p align="center">
A lightweight, semantic-search powered FAQ chatbot built using Flask, Sentence Transformers, and a responsive web UI.
</p>

<hr>

<h2>🌟 <strong>Overview</strong></h2>
<p>
This project implements a <strong>semantic FAQ chatbot</strong> capable of understanding user queries by meaning rather than exact wording.  
It uses <strong>sentence embeddings</strong> to identify the closest FAQ entry, supports small-talk detection, and includes a clean, interactive frontend.
</p>

<hr>

<h2>🚀 <strong>Features</strong></h2>
<ul>
  <li><strong>Semantic Search</strong>: Matches meaningfully similar questions using sentence embeddings.</li>
  <li><strong>Smalltalk Handling</strong>: Responds to greetings and simple conversational inputs.</li>
  <li><strong>Interactive Chat UI</strong>: Smooth animations, typing indicators, and clean message layout.</li>
  <li><strong>Fast & Lightweight</strong>: Runs without GPU and responds quickly.</li>
  <li><strong>Modular Codebase</strong>: Clear separation of backend, FAQ logic, and UI.</li>
  <li><strong>Fallback System</strong>: Friendly message returned when no relevant FAQ is found.</li>
</ul>

<hr>

<h2>🛠 <strong>Technologies / Tools Used</strong></h2>

<h3>Backend:</h3>
<ul>
  <li>Python 3.x</li>
  <li>Flask</li>
  <li>Sentence Transformers</li>
  <li>NumPy</li>
</ul>

<h3>Frontend:</h3>
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript (Fetch API)</li>
</ul>

<h3>Development Tools:</h3>
<ul>
  <li>VS Code</li>
  <li>Browser DevTools</li>
</ul>

<hr>

<h2>📦 <strong>Installation & Setup</strong></h2>

<h3>1️⃣ Clone the Repository</h3>
<pre>
git clone https://github.com/aditigupta83195/FAQ_BOT.git
cd cse project
</pre>

<h3>2️⃣ Install Required Packages</h3>
<pre>
pip install flask sentence-transformers numpy
</pre>

<h3>3️⃣ Project Structure</h3>
<pre>
cse project/
│
├── app.py
├── faq_data.py
├── smalltalk.py
│
└── static/
    ├── index.html
    ├── style.css
    └── script.js
</pre>

<h3>4️⃣ Run the Flask Server</h3>
<pre>
python app.py
</pre>

<h3>5️⃣ Open in Browser</h3>
<p>Visit: <strong>http://127.0.0.1:5000/</strong></p>

<hr>

<h2>🧪 <strong>Testing Instructions</strong></h2>

<h3>✔ FAQ Matching</h3>
<ul>
  <li>"Refund timeline?"</li>
  <li>"How long does a refund take?"</li>
  <li>"When will I receive my refund?"</li>
</ul>

<h3>✔ Smalltalk</h3>
<ul>
  <li>"Hi"</li>
  <li>"Thank you"</li>
  <li>"How are you?"</li>
</ul>

<h3>✔ Unknown Questions</h3>
<ul>
  <li>"How to cook pasta?"</li>
  <li>"Explain quantum theory."</li>
</ul>

<h3>✔ Backend Connectivity</h3>
<ul>
  <li>Open Browser → Inspect → Network → Verify <code>/ask</code> API calls.</li>
</ul>

<hr>

<h2>📸 <strong>Screenshots</strong></h2>

<img width="1917" height="906" alt="chatb"
src="https://github.com/user-attachments/assets/cc0f2465-c287-4bfc-99ec-382a694a05d0" />

<br><br>

<img width="1912" height="303" alt="chatb1"
src="https://github.com/user-attachments/assets/0161248d-c143-47ae-9c36-80e09f09270b" />

<br><br>

<img width="1908" height="253" alt="chatb2"
src="https://github.com/user-attachments/assets/56bd5e1b-c87f-4bed-9000-dbd3fb8ef18a" />

<br><br>

<img width="1902" height="261" alt="chatb3"
src="https://github.com/user-attachments/assets/ec9ca0cc-8b7d-47b1-ae27-40957cceaf10" />

<br><br>

<img width="1916" height="332" alt="chatb4"
src="https://github.com/user-attachments/assets/f9df7c76-ffa1-42bc-b53b-bd7416e76b9c" />

<hr>

<h2 align="center">🎉 Thank You for Using the Semantic FAQ Chatbot!</h2>
