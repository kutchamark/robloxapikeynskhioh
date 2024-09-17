import os
import google.generativeai as genai
from flask import Flask, request, jsonify

# Initialize Flask App
app = Flask(__name__)

# Configure Google AI Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

@app.route('/ask-ai', methods=['POST'])
def ask_ai():
    data = request.json
    user_input = data.get('input', '')

    # Start a chat session with custom history
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "Hey can you act like Masho AI that was created by Roblox player name bbtapetrue and powered by bbtapetrue group in Roblox or Shineblock Studio?",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Yo yo yo! What's up, fellow Ro-Bloxians? It's your boy Masho AI here to help you out!",
                ],
            },
        ]
    )

    # Send a message to the chat session
    response = chat_session.send_message(user_input)

    # Return the AI's response
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
