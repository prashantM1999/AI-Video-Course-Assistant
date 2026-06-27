const sendButton = document.getElementById("send-btn");
const questionBox = document.getElementById("question");
const chatBox = document.getElementById("chat-box");


function addMessage(message, className) {

    const div = document.createElement("div");

    div.className = className;

    div.innerHTML = message;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;

}


async function sendQuestion() {

    const question = questionBox.value.trim();

    if (question === "") {
        return;
    }

    // Show user message

    addMessage("👤 " + question, "user-message");

    questionBox.value = "";

    // Loading message

    const loading = document.createElement("div");

    loading.className = "bot-message";

    loading.innerHTML = "🤖 Thinking...";

    chatBox.appendChild(loading);

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                question: question

            })

        });

        const data = await response.json();

        loading.remove();

        if (data.video_title === "") {
            addMessage(`
                <div class = "answer-card">
                <h3>🤖 AI Assistent</h3>
                <p>${data.answer}<p>
                </div>
                `, "bot-message")
        } else {

            addMessage(

                `
        <h3>🤖 AI Assistant</h3>

        <p><strong>📹 Video :</strong> ${data.video_title}</p>

        <p><strong>🎬 Video Number :</strong> ${data.video_number}</p>

        <p><strong>⏰ Timestamp :</strong> ${Math.floor(data.start_time / 60)}:${String(Math.floor(data.start_time % 60)).padStart(2, '0')}</p>

        <hr>

        <p>${data.answer}</p>

        ` , "bot-message");
        }

    }

    catch (error) {

        loading.remove();

        addMessage("❌ Error communicating with server.", "bot-message");

    }

}


sendButton.addEventListener("click", sendQuestion);


questionBox.addEventListener("keypress", function (event) {

    if (event.key === "Enter" && !event.shiftKey) {

        event.preventDefault();

        sendQuestion();

    }

});