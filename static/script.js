
let chatHistory = JSON.parse(localStorage.getItem("chatHistory")) || [];


window.onload = () => {
    chatHistory.forEach(msg => addMessage(msg.text, msg.sender, false));
};


function saveHistory() {
    localStorage.setItem("chatHistory", JSON.stringify(chatHistory));
}


function addMessage(text, sender, save = true) {
    const box = document.getElementById("chat-box");

    const msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.innerHTML = text;

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


async function sendToBackend(userMsg) {
    const res = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userMsg })
    });

    const data = await res.json();
    return data.answer;
}


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

    if (document.getElementById("voiceToggle").value === "on") {
        speakMessage(reply);
    }
}


function speakMessage(text) {
    const voiceSetting = document.getElementById("voiceToggle").value;
    if (voiceSetting === "off") return;

    const speak = new SpeechSynthesisUtterance(text);
    speak.lang = "en-US";
    speak.rate = 1;
    speak.pitch = 1;

    window.speechSynthesis.speak(speak);
}


document.getElementById("newChat").onclick = () => {
    localStorage.removeItem("chatHistory");
    document.getElementById("chat-box").innerHTML = "";
    chatHistory = [];
};
