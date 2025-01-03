function sendMessage() {
    let userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return;

    // Display user's message
    displayMessage(userInput, "user");

    // Clear input field
    document.getElementById("user-input").value = "";

    // Show typing indicator
    toggleTypingIndicator(true);

    // Make API request to the deployed backend
    fetch("https://meditrain-ai-11.onrender.com/response", {
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
            if (data.response) {
                displayMessage(data.response, "bot");
            } else {
                displayMessage("The chatbot did not return a valid response.", "bot");
            }
        })
        .catch((error) => {
            console.error("Error:", error);

            // Hide typing indicator
            toggleTypingIndicator(false);

            displayMessage("Oops! Something went wrong. Please try again later.", "bot");
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
