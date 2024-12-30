 Meditrain AI Chatbot

Meditrain AI is an intelligent chatbot that simulates a doctor's role by assessing symptoms and providing suggestions or prescription-like recommendations. The project includes a robust backend, an interactive frontend, and uses Postman for API testing.


 Features

- AI-Powered Symptom Analysis: Analyzes user input for health-related suggestions.
- Prescription Simulation: Offers responses similar to those from healthcare professionals.
- Dynamic User Interface: Intuitive chat-based interaction.
- Postman API Support: Easily test API responses for debugging.
- Customizable Design: Includes a `style.css` for personalized UI.

---

 Project Structure

- Backend:
  - File: `backend.py`
  - Features:
    - Built with Flask and LangChain.
    - Integrated Groq-based AI model for conversational memory.
    - RESTful API accessible via Postman for testing and debugging.

- Frontend:
  - Files: 
    - `index.html`: The main UI for user interaction.
    - `style.css`: Custom styles for enhancing the chatbot interface.
    - `script.js`: JavaScript functionality for dynamic chat interactions.

---

 Prerequisites

- Python 3.8+
- Flask
- Postman (for API testing)
- A `.env` file with the `API_KEY` for Groq AI model

---

Backend Setup

  Install Dependencies:pip install -r requirements.txt

Set Environment Variables: Create a .env file with:API_KEY=your_groq_api_key
Run the Backend:python backend.py
Backend runs on http://127.0.0.1:5000.

Frontend Setup

    Ensure the backend is running.
    Open index.html in a browser.
    The frontend communicates with the /response API for chatbot replies.

API Testing with Postman

  Start Backend: Ensure the backend server is running.

  Configure Postman:
        Open Postman.Create a new request:
        Method: POST
            URL: http://127.0.0.1:5000/response
        Add the following JSON to the request body:

    {
      "query": "Describe your symptoms here"
    }

    Send the request to test the chatbot's response.

Expected Response:

    {
      "response": "Doctor-like prescription or suggestion"
    }

Usage

    Start the backend server.
    Open the index.html file in a web browser.
    Enter symptoms or questions in the chat input.
    The chatbot will respond with tailored suggestions or prescriptions.
