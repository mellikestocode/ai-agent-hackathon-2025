#!/bin/bash

# ChatGPT Clone - Complete Application Startup Script

echo "🎉 ChatGPT Clone - Starting Complete Application"
echo "=============================================="
echo ""

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to start backend in background
start_backend() {
    echo "🔧 Starting Backend Server..."
    cd backend
    
    # Make start script executable
    chmod +x start.sh
    
    # Start backend in background
    ./start.sh &
    BACKEND_PID=$!
    
    echo "✅ Backend server started (PID: $BACKEND_PID)"
    echo "   Backend URL: http://localhost:5000"
    echo ""
    
    cd ..
}

# Function to start frontend
start_frontend() {
    echo "🎨 Starting Frontend Server..."
    cd frontend
    
    # Make start script executable
    chmod +x start.sh
    
    # Start frontend (this will block)
    ./start.sh
    
    cd ..
}

# Function to cleanup background processes
cleanup() {
    echo ""
    echo "🛑 Shutting down servers..."
    
    if [ ! -z "$BACKEND_PID" ]; then
        kill $BACKEND_PID 2>/dev/null
        echo "✅ Backend server stopped"
    fi
    
    # Kill any remaining Python processes running our app
    pkill -f "python app.py" 2>/dev/null
    
    echo "👋 Goodbye!"
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Check prerequisites
echo "🔍 Checking prerequisites..."

if ! command_exists python3; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3 from https://python.org/"
    exit 1
fi

if ! command_exists node; then
    echo "❌ Node.js is required but not installed."
    echo "Please install Node.js from https://nodejs.org/"
    exit 1
fi

if ! command_exists npm; then
    echo "❌ npm is required but not installed."
    exit 1
fi

echo "✅ All prerequisites are installed"
echo ""

# Start backend
start_backend

# Wait a moment for backend to start
echo "⏳ Waiting for backend to initialize..."
sleep 3

# Test backend connectivity
echo "🔗 Testing backend connectivity..."
if curl -f http://localhost:5000/ >/dev/null 2>&1; then
    echo "✅ Backend is responding"
else
    echo "⚠️  Backend might still be starting up"
fi
echo ""

# Start frontend (this will block until Ctrl+C)
start_frontend

# Cleanup will be called by the trap