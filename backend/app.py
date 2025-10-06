from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import uuid
import random
from openai import OpenAI
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

# In-memory storage for chat sessions (in production, use a database)
chat_sessions = {}

client = OpenAI()

@app.route('/', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Clompanion AI API is running!"})

@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({"error": "Message is required"}), 400
        
        user_message = data['message'].strip()
        session_id = data.get('session_id', str(uuid.uuid4()))
        
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400
        
        # Initialize session if it doesn't exist
        if session_id not in chat_sessions:
            chat_sessions[session_id] = {
                'messages': [],
                'created_at': time.time()
            }
        
        # Add user message to session
        user_msg = {
            'id': str(uuid.uuid4()),
            'role': 'user',
            'content': user_message,
            'timestamp': time.time()
        }
        chat_sessions[session_id]['messages'].append(user_msg)

        # TODO: Grab patient medical record
        medical_history = fetch_medical_record()  # Placeholder
        
        # TODO: Generate AI response
        ai_response = generate_ai_response(user_message, medical_history, chat_sessions[session_id]['messages'])
        
        ai_msg = {
            'id': str(uuid.uuid4()),
            'role': 'assistant',
            'content': ai_response,
            'timestamp': time.time()
        }
        chat_sessions[session_id]['messages'].append(ai_msg)
        
        return jsonify({
            'session_id': session_id,
            'response': ai_response,
            'message_id': ai_msg['id']
        })
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route('/api/chat/<session_id>/history', methods=['GET'])
def get_chat_history(session_id):
    """Get chat history for a session"""
    if session_id not in chat_sessions:
        return jsonify({"error": "Session not found"}), 404
    
    return jsonify({
        'session_id': session_id,
        'messages': chat_sessions[session_id]['messages']
    })

@app.route('/api/chat/<session_id>', methods=['DELETE'])
def clear_chat(session_id):
    """Clear chat history for a session"""
    if session_id in chat_sessions:
        del chat_sessions[session_id]
    
    return jsonify({"message": "Chat history cleared"})

@app.route('/api/sessions', methods=['GET'])
def get_sessions():
    """Get all active sessions"""
    sessions = []
    for session_id, session_data in chat_sessions.items():
        sessions.append({
            'session_id': session_id,
            'created_at': session_data['created_at'],
            'message_count': len(session_data['messages'])
        })
    
    return jsonify({'sessions': sessions})

def fetch_medical_record():
    """Fetch mock medical record"""
    with open('mock_medical_record.json', 'r') as file:
        medical_record = json.load(file)
    return medical_record

def generate_ai_response(user_message, medical_history, conversation_history):
    """Generate a mock AI response"""
    response = client.responses.create(
        model="gpt-5-mini",
        input=user_message.lower()
    )
    return response.output_text

    

if __name__ == '__main__':
    print("Starting Clompanion AI Backend...")
    print("API will be available at: http://localhost:5000")
    print("Health check: http://localhost:5555/")
    app.run(debug=True, host='0.0.0.0', port=5000)