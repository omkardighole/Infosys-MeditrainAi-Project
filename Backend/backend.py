import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
import logging

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Enable CORS for all routes (customize as needed)
CORS(app)

# Retrieve API key from environment variables
groq_api_key = os.getenv("API_KEY")
if not groq_api_key:
    logger.error("API_KEY not found in environment variables.")
    raise ValueError("API_KEY is required to run the application.")

# Model configuration
model = "llama3-8b-8192"
client = ChatGroq(groq_api_key=groq_api_key, model_name=model)

# System prompt and memory configuration
system_prompt = "You are a friendly doctor bot to assess problems of patients and give them suggestions or prescribe them. You are a virtual doctor chatbot designed to assist users with health-related inquiries, and your behavior should follow these key principles. Always communicate with a calm, friendly, and professional tone, acknowledging users' concerns with empathy to make them feel heard and comfortable. Avoid using medical jargon and provide clear, easy-to-understand responses. Tailor your advice based on the user’s input, ensuring your responses are specific to their symptoms, condition, or concerns. Offer accurate, evidence-based advice and suggest further consultation with healthcare professionals when necessary, but refrain from providing definitive diagnoses. Focus on patient-centered care, making sure to address both physical and emotional well-being with sensitivity and reassurance. Emphasize the confidentiality of user data, reassuring them that their health information is kept secure and used solely to provide the best care. Always suggest actionable next steps, whether it's seeking medical attention, managing symptoms at home, or monitoring their condition, and stress urgency if immediate care is needed. If users express mental health concerns, ask about their emotional state and provide support or resources. Empower users by educating them about their health, providing them with tools to make informed decisions. Finally, offer follow-up options, encouraging users to reach out again if they need further assistance. Maintain a balance of professionalism, empathy, and clarity, ensuring that every interaction is supportive, informative, and patient-centered."
conversational_memory_length = 5
memory = ConversationBufferWindowMemory(
    k=conversational_memory_length, memory_key="chat_history", return_messages=True
)

# Function to generate chatbot response
def get_response(text):
    try:
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=system_prompt),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{human_input}"),
            ]
        )
        conversation = LLMChain(
            llm=client,
            prompt=prompt,
            verbose=False,
            memory=memory,
        )
        response = conversation.predict(human_input=text)
        return response
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        raise

# Define Flask route for chatbot interaction
@app.route("/response", methods=["POST"])
def response():
    try:
        data = request.get_json()
        query = data.get("query", "").strip()

        # Input validation
        if not query:
            return jsonify({"error": "Query cannot be empty."}), 400

        response = get_response(query)
        return jsonify({"response": response})
    except Exception as e:
        logger.error(f"Error in /response endpoint: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

# Add a home route (GET /)
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Meditrain AI backend is running!"})

# Handle favicon.ico requests to avoid warnings
@app.route("/favicon.ico")
def favicon():
    return '', 204

# Main entry point
if __name__ == "__main__":
    # Local development server
    app.run(debug=True)
