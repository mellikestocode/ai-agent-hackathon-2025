from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import uuid
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

# In-memory storage for chat sessions (in production, use a database)
chat_sessions = {}

# Mock AI responses for demonstration
MOCK_RESPONSES = [
    "That's an interesting question! Let me think about that for a moment.",
    "I understand what you're asking. Here's my perspective on that topic.",
    "Based on what you've shared, I think there are a few ways to approach this.",
    "That's a great point! Let me elaborate on that idea.",
    "I can help you with that. Here are some suggestions:",
    "From my understanding, this is a common question that many people have.",
    "Let me break this down for you in a clear and helpful way.",
    "That's exactly the kind of question I love to help with!",
]

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
        
        # Generate AI response (mock)
        ai_response = generate_ai_response(user_message, chat_sessions[session_id]['messages'])
        
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

def generate_ai_response(user_message, conversation_history):
    """Generate a mock AI response"""
    # Simple mock response generation
    user_message_lower = user_message.lower()
    
    # Context-aware responses
    if 'hello' in user_message_lower or 'hi' in user_message_lower:
        return "Hello! I'm here to help you with any questions or tasks you have. What would you like to talk about?"
    
    elif 'how are you' in user_message_lower:
        return "I'm doing great, thank you for asking! I'm here and ready to help you with whatever you need."
    
    elif 'what is' in user_message_lower or 'define' in user_message_lower:
        return f"Great question about '{user_message}'. Let me provide you with a comprehensive explanation based on what I know."
    
    elif 'help' in user_message_lower:
        return "I'd be happy to help! I can assist with answering questions, explaining concepts, helping with problems, or just having a conversation. What specific area would you like help with?"
    
    elif '?' in user_message:
        base_response = random.choice(MOCK_RESPONSES)
        return f"{base_response} Regarding your question: '{user_message}' - this is something I can definitely help clarify for you."
    
    else:
        return random.choice(MOCK_RESPONSES) + f" You mentioned: '{user_message}' - that's definitely worth exploring further!"

if __name__ == '__main__':
    print("Starting Clompanion AI Backend...")
    print("API will be available at: http://localhost:5000")
    print("Health check: http://localhost:5000/")
    app.run(debug=True, host='0.0.0.0', port=5000)