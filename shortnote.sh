#!/bin/bash

# Navigate to the project directory
cd /home/ducky/Desktop/myprojects/hacking-helper || {
  echo "❌ Project directory not found!"
  exit 1
}

# Activate virtual environment
source venv/bin/activate || {
  echo "❌ Failed to activate virtual environment!"
  exit 1
}

# Start backend
cd backend || {
  echo "❌ Backend directory not found!"
  exit 1
}
echo "🚀 Starting backend server on port 8000..."
uvicorn main:app --reload --host 0.0.0.0 --port 8000 &

# Wait a second to ensure backend starts before frontend
sleep 1

# Start frontend
cd ../frontend || {
  echo "❌ Frontend directory not found!"
  exit 1
}
echo "🌐 Starting frontend server on port 5500..."
python3 -m http.server 5500 &

# Final status message
echo "✅ ShortNote website successfully running!"
echo "🔗 Backend: http://localhost:8000"
echo "🔗 Frontend: http://localhost:5500"
