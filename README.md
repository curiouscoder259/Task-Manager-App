# 🚀 AI-Powered Task Manager

A full-stack web application that combines traditional task management with generative AI to help users prioritize their workload. Built with React, Flask, and Google's Gemini API.

## ✨ Key Features
* **Secure Authentication:** JWT-based user registration and login system.
* **CRUD Operations:** Create and manage daily tasks with ease.
* **AI Priority Engine:** Integrates with the `gemini-2.5-flash` model to analyze task descriptions and automatically suggest a priority level (Low/Medium/High) and a concrete next step.
* **RESTful Architecture:** Clean separation of concerns between the React client and the Flask API.

## 🛠️ Tech Stack
* **Frontend:** React.js, Axios, React Router
* **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-JWT-Extended
* **Database:** SQLite (Development)
* **AI Integration:** Google Generative AI SDK (Gemini 2.5 Flash)

## 🚦 Local Setup Instructions

### 1. Backend Setup
Navigate to the backend directory and set up your Python environment:
```bash
cd backend
python -m venv venv
source venv/Scripts/activate  # (On Windows use: .\venv\Scripts\activate)
pip install -r requirements.txt




Create a .env file in the /backend folder with the following variables:

DATABASE_URL=sqlite:///app.db
JWT_SECRET_KEY=your_secure_secret_key
GEMINI_API_KEY=your_gemini_api_key_here

Initialize the database and run the server:

flask db upgrade
python run.py

Let's get this portfolio-ready! Since you are preparing for software engineering roles, your README and video shouldn't just show that the code works—they need to show that you think like a professional engineer. Recruiters love clean documentation and a demonstration of how you handle modern API integrations.

Here is a complete toolkit for your submission.

Part 1: The "Hire Me" README Template
Copy this directly into a README.md file in the root of your project. It is formatted using Markdown, so it will look beautiful on GitHub.

Markdown
# 🚀 AI-Powered Task Manager

A full-stack web application that combines traditional task management with generative AI to help users prioritize their workload. Built with React, Flask, and Google's Gemini API.

## ✨ Key Features
* **Secure Authentication:** JWT-based user registration and login system.
* **CRUD Operations:** Create and manage daily tasks with ease.
* **AI Priority Engine:** Integrates with the `gemini-2.5-flash` model to analyze task descriptions and automatically suggest a priority level (Low/Medium/High) and a concrete next step.
* **RESTful Architecture:** Clean separation of concerns between the React client and the Flask API.

## 🛠️ Tech Stack
* **Frontend:** React.js, Axios, React Router
* **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-JWT-Extended
* **Database:** SQLite (Development)
* **AI Integration:** Google Generative AI SDK (Gemini 2.5 Flash)

## 🚦 Local Setup Instructions

### 1. Backend Setup
Navigate to the backend directory and set up your Python environment:
```bash
cd backend
python -m venv venv
source venv/Scripts/activate  # (On Windows use: .\venv\Scripts\activate)
pip install -r requirements.txt
Create a .env file in the /backend folder with the following variables:

Code snippet
DATABASE_URL=sqlite:///app.db
JWT_SECRET_KEY=your_secure_secret_key
GEMINI_API_KEY=your_gemini_api_key_here
Initialize the database and run the server:

Bash
flask db upgrade
python run.py



2. Frontend Setup
Open a new terminal, navigate to the frontend directory, and start the React app:

cd frontend
npm install
npm start




Markdown
# 🚀 AI-Powered Task Manager

A full-stack web application that combines traditional task management with generative AI to help users prioritize their workload. Built with React, Flask, and Google's Gemini API.

## ✨ Key Features
* **Secure Authentication:** JWT-based user registration and login system.
* **CRUD Operations:** Create and manage daily tasks with ease.
* **AI Priority Engine:** Integrates with the `gemini-2.5-flash` model to analyze task descriptions and automatically suggest a priority level (Low/Medium/High) and a concrete next step.
* **RESTful Architecture:** Clean separation of concerns between the React client and the Flask API.

## 🛠️ Tech Stack
* **Frontend:** React.js, Axios, React Router
* **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-JWT-Extended
* **Database:** SQLite (Development)
* **AI Integration:** Google Generative AI SDK (Gemini 2.5 Flash)

## 🚦 Local Setup Instructions

### 1. Backend Setup
Navigate to the backend directory and set up your Python environment:
```bash
cd backend
python -m venv venv
source venv/Scripts/activate  # (On Windows use: .\venv\Scripts\activate)
pip install -r requirements.txt
Create a .env file in the /backend folder with the following variables:

Code snippet
DATABASE_URL=sqlite:///app.db
JWT_SECRET_KEY=your_secure_secret_key
GEMINI_API_KEY=your_gemini_api_key_here
Initialize the database and run the server:

Bash
flask db upgrade
python run.py
2. Frontend Setup
Open a new terminal, navigate to the frontend directory, and start the React app:

Bash
cd frontend
npm install
npm start
🧠 Engineering Decisions

open a third terminal- run this command
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/auth/register -Method Post -ContentType "application/json" -Body '{"[email":"test@test.com](mailto:email%22:%22test@test.com)", "password":"password123"}'

Token-Based Auth: Chosen over session cookies to allow for a stateless API, making it easier to scale the backend independently.

Strict JSON Enforcement: Utilized Gemini's response_mime_type configuration to guarantee the AI returns valid JSON, preventing frontend parsing crashes and ensuring a seamless UI experience.

