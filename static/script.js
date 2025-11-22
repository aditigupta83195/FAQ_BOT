// Chat history is stored locally so it reloads after refresh
let chatHistory = JSON.parse(localStorage.getItem("chatHistory")) || [];

// This loads chat history onto the screen when page opens
window.onload = () => {
    chatHistory.forEach(msg => addMessage(msg.text, msg.sender, false));
};

// Save chat messages to localStorage
function saveHistory() {
    localStorage.setItem("chatHistory", JSON.stringify(chatHistory));
}

// Adds message to chat window
function addMessage(text, sender, save = true) {
    const box = document.getElementById("chat-box");

    const msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.innerHTML = text;

    // speaker icon for bot messages
    if (sender === "bot") {
        const btn = document.createElement("div");
        btn.classList.add("speak-btn");
        btn.innerHTML = "🔊";
        btn.onclick = () => speakMessage(text);
        msg.appendChild(btn);
    }

    box.appendChild(msg);
    box.scrollTop = box.scrollHeight;

    if (save) {
        chatHistory.push({ text, sender });
        saveHistory();
    }
}

// Sends message to Python backend
async function sendToBackend(userMsg) {
    const res = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userMsg })
    });

    const data = await res.json();
    return data.answer;
}

// Handles send button click
document.getElementById("send").onclick = handleSend;
document.getElementById("input").addEventListener("keypress", e => {
    if (e.key === "Enter") handleSend();
});

async function handleSend() {
    const input = document.getElementById("input");
    const msg = input.value.trim();
    if (!msg) return;

    addMessage(msg, "user");
    input.value = "";

    const reply = await sendToBackend(msg);
    addMessage(reply, "bot");

    // auto play voice if enabled
    if (document.getElementById("voiceToggle").value === "on") {
        speakMessage(reply);
    }
}

// Text-to-Speech function
function speakMessage(text) {
    const voiceSetting = document.getElementById("voiceToggle").value;
    if (voiceSetting === "off") return;

    const speak = new SpeechSynthesisUtterance(text);
    speak.lang = "en-US";
    speak.rate = 1;
    speak.pitch = 1;

    window.speechSynthesis.speak(speak);
}

// Clears chat history
document.getElementById("newChat").onclick = () => {
    localStorage.removeItem("chatHistory");
    document.getElementById("chat-box").innerHTML = "";
    chatHistory = [];
};
