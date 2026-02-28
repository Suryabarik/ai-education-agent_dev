# 🎯 AI Tutor Agent — Agentic Education System

An AI-powered multi-agent education system that generates grade-wise explanations, creates MCQs, reviews content quality, and automatically refines outputs.

This project demonstrates an **AI-native, agent-based architecture** built for scalable EdTech applications.

---

⚙️ How the System Works

The AI Tutor Agent follows a two-tier architecture:

🔹 FastAPI Backend — handles AI logic and APIs

🔹 Streamlit Frontend — provides user interface

Both services run separately but communicate via HTTP APIs.

🔧 Backend — How It Works

The backend is built using FastAPI and is responsible for:

Running the Generator Agent

Running the Reviewer Agent

Managing the refinement loop

Calling the Groq LLM

Returning structured JSON responses

▶️ Start the Backend

From the backend folder:

uvicorn main:app --reload
✅ Expected Output
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
🌐 Backend Endpoint Flow
Frontend Request → FastAPI → Generator Agent → Reviewer Agent → Refinement → Response

When the backend is running:

API base URL:

http://127.0.0.1:8000

Interactive docs available at:

http://127.0.0.1:8000/docs
🎨 Frontend — How It Works

The frontend is built using Streamlit and is responsible for:

Collecting user input (topic, grade, etc.)

Sending requests to the FastAPI backend

Displaying explanations and MCQs

Showing refined output

⚠️ Important: Frontend does NOT run AI directly — it calls the backend API.

▶️ Start the Frontend

From the frontend folder:

streamlit run app.py
✅ Expected Output
Local URL: http://localhost:8501

Open this URL in your browser.

🔄 Frontend–Backend Communication

The Streamlit app sends HTTP requests to FastAPI.

Flow:
User → Streamlit UI → FastAPI API → AI Agents → Response → Streamlit Display
⚠️ Important Setup Notes

✅ Start backend first
✅ Then start frontend
✅ Ensure backend URL in Streamlit is correct

Example inside app.py:

API_BASE_URL = "http://127.0.0.1:8000"
🧪 How to Verify Everything Works
Step 1 — Backend check

Open:

http://127.0.0.1:8000/docs

If Swagger UI opens → backend is working ✅

Step 2 — Frontend check

Open:

http://localhost:8501

If Streamlit UI appears → frontend is working ✅

Step 3 — End-to-end test

Enter a topic

Select grade

Click generate

Verify explanation + MCQs appear

✅ If yes → full pipeline working


