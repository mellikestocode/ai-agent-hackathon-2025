#!/bin/bash

# ChatGPT Clone Backend Startup Script

echo "🚀 Starting ChatGPT Clone Backend..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if virtual environment exists, create if not
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Start the Flask server
echo "🌐 Starting Flask server on http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo ""
python app.py