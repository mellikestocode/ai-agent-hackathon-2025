#!/bin/bash

# Clompanion AI Frontend Startup Script

echo "🚀 Starting Clompanion AI Frontend..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed."
    echo "Please install Node.js from https://nodejs.org/"
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is required but not installed."
    exit 1
fi

# Install dependencies if node_modules doesn't exist
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

# Start the React development server
echo "🌐 Starting React development server on http://localhost:3000"
echo "The browser should open automatically"
echo "Press Ctrl+C to stop the server"
echo ""
npm start