function sendMessage() {
    let userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return;

    // Display user's message
    displayMessage(userInput, "user");

    // Clear input field
    document.getElementById("user-input").value = "";

    // Show typing indicator
    toggleTypingIndicator(true);

    // Make API request to backend
    fetch("http://127.0.0.1:5000/response", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ query: userInput }),
    })
        .then((response) => response.json())
        .then((data) => {
            // Hide typing indicator
            toggleTypingIndicator(false);

            // Display chatbot's response
            displayMessage(data.response, "bot");
        })
        .catch((error) => {
            console.error("Error:", error);

            // Hide typing indicator
            toggleTypingIndicator(false);

            displayMessage("Oops! Something went wrong.", "bot");
        });
}

function displayMessage(message, sender) {
    const chatBox = document.getElementById("chat-box");

    const messageDiv = document.createElement("div");
    messageDiv.className = `chat-message ${sender === "user" ? "user-message" : "bot-message"}`;
    messageDiv.textContent = message;

    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function toggleTypingIndicator(show) {
    const typingIndicator = document.getElementById("typing-indicator");
    typingIndicator.style.display = show ? "flex" : "none";
}
