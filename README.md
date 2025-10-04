# Clompanion AI 🤖💬

Project Overview: The Clinical AI Companion
The Problem:
Doctors today are overwhelmed. They face immense cognitive load from navigating complex, clunky Electronic Health Record (EHR) systems. Sifting through years of patient data—labs, notes, and scans—is time-consuming and can lead to missed details, diagnostic errors, and physician burnout.

Our Solution:
The Clinical AI Companion is an intelligent, conversational assistant designed for healthcare professionals. It acts as a smart layer on top of existing EHRs, allowing doctors to simply ask questions in natural language instead of manually hunting for information. It's like having a personal data analyst available 24/7.

How It Works:
Using advanced Natural Language Processing (NLP) and Large Language Models (LLMs), our system understands complex medical queries. A doctor can ask:

"What are the latest lab results for Jane Doe?"

"Show me all my diabetic patients with poor blood sugar control."

"Summarize John Smith's cardiac history and flag any risks for his upcoming surgery."

The AI instantly retrieves, synthesizes, and presents the most relevant information in a clear, concise summary.

![Clompanion AI Preview](https://img.shields.io/badge/Status-Ready%20to%20Use-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![React](https://img.shields.io/badge/React-18+-61DAFB)
![Flask](https://img.shields.io/badge/Flask-3.0+-green)

## 🌟 Features

### Frontend (React)
- **Modern Chat Interface** - Clean, responsive design similar to ChatGPT
- **Real-time Messaging** - Instant message display with smooth animations
- **Typing Indicators** - Visual feedback when AI is "thinking"
- **Message History** - Persistent conversation within sessions
- **Auto-scroll** - Automatically scrolls to latest messages
- **Responsive Design** - Works perfectly on desktop and mobile
- **Error Handling** - Graceful handling of network issues

### Backend (Flask)
- **RESTful API** - Clean API endpoints for chat functionality
- **Session Management** - Track multiple chat sessions
- **CORS Support** - Proper cross-origin resource sharing
- **Mock AI Responses** - Context-aware responses for demonstration
- **Health Checks** - API status monitoring
- **Error Handling** - Robust error handling and logging

## 🚀 Quick Start

### Option 1: One-Command Setup (Recommended)
```bash
# Clone and start everything at once
git clone <repository-url>
cd chatgpt-clone
chmod +x start.sh
./start.sh
```

The script will:
1. ✅ Check prerequisites (Python 3, Node.js, npm)
2. 🔧 Start the backend server (http://localhost:5000)
3. 🎨 Start the frontend server (http://localhost:3000)
4. 🌐 Open your browser automatically

### Option 2: Manual Setup

#### Prerequisites
- **Python 3.8+** - [Download here](https://python.org/)
- **Node.js 16+** - [Download here](https://nodejs.org/)
- **npm** (comes with Node.js)

#### Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

#### Frontend Setup (in a new terminal)
```bash
cd frontend
npm install
npm start
```

## 📁 Project Structure

```
chatgpt-clone/
├── backend/                 # Flask backend
│   ├── app.py              # Main Flask application
│   ├── requirements.txt    # Python dependencies
│   └── start.sh           # Backend startup script
├── frontend/               # React frontend
│   ├── public/
│   │   └── index.html     # HTML template
│   ├── src/
│   │   ├── App.js         # Main React component
│   │   ├── App.css        # Styling
│   │   ├── index.js       # React entry point
│   │   └── index.css      # Base styles
│   ├── package.json       # React dependencies
│   └── start.sh          # Frontend startup script
├── start.sh               # Complete app startup script
└── README.md             # This documentation
```

## 🔧 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### Health Check
```http
GET /
```
**Response:**
```json
{
  "status": "healthy",
  "message": "Clompanion AI API is running!"
}
```

#### Send Chat Message
```http
POST /api/chat
```
**Request Body:**
```json
{
  "message": "Hello, how are you?",
  "session_id": "optional-session-id"
}
```
**Response:**
```json
{
  "session_id": "uuid-string",
  "response": "Hello! I'm doing great, thank you for asking!",
  "message_id": "message-uuid"
}
```

#### Get Chat History
```http
GET /api/chat/{session_id}/history
```
**Response:**
```json
{
  "session_id": "uuid-string",
  "messages": [
    {
      "id": "message-uuid",
      "role": "user",
      "content": "Hello!",
      "timestamp": 1634567890.123
    },
    {
      "id": "message-uuid",
      "role": "assistant",
      "content": "Hi there!",
      "timestamp": 1634567891.456
    }
  ]
}
```

#### Clear Chat History
```http
DELETE /api/chat/{session_id}
```

#### Get All Sessions
```http
GET /api/sessions
```

## 🎨 Customization

### Adding Real AI Integration

To integrate with a real AI service (like OpenAI's GPT), modify the `generate_ai_response` function in `backend/app.py`:

```python
import openai

def generate_ai_response(user_message, conversation_history):
    # Replace with actual OpenAI API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content
```

### Styling Customization

Modify `frontend/src/App.css` to change:
- Color scheme (update CSS variables)
- Layout dimensions
- Animations and transitions
- Typography

### Adding Features

Easy areas to extend:
- **File uploads** - Add image/document sharing
- **Voice messages** - Integrate speech-to-text
- **Chat export** - Download conversation history
- **User authentication** - Add login/signup
- **Multiple AI models** - Support different AI backends

## 🐛 Troubleshooting

### Port Already in Use
If you get port errors:

**Backend (port 5000):**
```bash
# Kill process using port 5000
lsof -ti:5000 | xargs kill -9
```

**Frontend (port 3000):**
```bash
# Kill process using port 3000
lsof -ti:3000 | xargs kill -9
```

### CORS Issues
If you get CORS errors, ensure:
1. Flask-CORS is installed: `pip install Flask-CORS`
2. Backend is running before frontend
3. Frontend proxy is configured (already set in package.json)

### Dependencies Issues
```bash
# Backend: Clear and reinstall
cd backend
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend: Clear and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install
```

## 🔒 Security Notes

⚠️ **This is a development/demo application**

For production use, implement:
- **Authentication & Authorization**
- **Rate limiting**
- **Input sanitization**
- **HTTPS/TLS encryption**
- **Database persistence** (currently uses in-memory storage)
- **Environment variables** for sensitive configuration
- **Proper logging and monitoring**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋‍♂️ Support

If you encounter issues:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Ensure all prerequisites are installed
3. Verify ports 3000 and 5000 are available
4. Check browser console for frontend errors
5. Check terminal output for backend errors

---

**Made with ❤️ using React and Flask**

*Happy chatting! 🎉*