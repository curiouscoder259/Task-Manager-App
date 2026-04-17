
# 🚀 AI-Powered Task Manager

A full-stack task management application that integrates Google's Gemini AI to analyze tasks, determine priority, and suggest actionable next steps. Built with a modern tech stack featuring React, Flask, PostgreSQL, and Tailwind CSS.

## ✨ Features
* **Full Authentication:** Secure user registration, login, and logout using JWT (JSON Web Tokens).
* **AI Task Strategy:** Integrates `gemini-2.5-flash` to automatically generate intelligent priorities and actionable "next steps" based on task titles and descriptions.
* **Production-Ready Database:** Utilizes PostgreSQL for robust, relational data storage.
* **Modern UI/UX:** Fully responsive and styled using Tailwind CSS (v3) for a clean, intuitive user experience.
* **User Profiles:** Dedicated profile dashboard mapping user sessions to database records.
* **Full CRUD:** Create, Read, and Delete tasks mapped directly to specific authenticated users.

## 🛠️ Tech Stack
**Frontend:**
* React.js
* Tailwind CSS (v3)
* React Router DOM (Navigation)
* Axios (API Client)

**Backend:**
* Python / Flask
* Flask-SQLAlchemy (ORM)
* Flask-Migrate (Alembic Database Migrations)
* Flask-JWT-Extended (Authentication)
* Google GenAI SDK

**Database:**
* PostgreSQL

---

## 💻 Local Installation & Setup

### Prerequisites
* Python 3.9+
* Node.js & npm
* PostgreSQL (pgAdmin or psql)

### 1. Database Setup
Before running the application, you must create a local PostgreSQL database.
1. Open pgAdmin.
2. Create a new database named `task_manager_db`.

### 2. Backend Setup
Navigate to the backend directory and set up your virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt


<!-- # Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify) -->


Create a .env file in the backend directory and add the following:
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_super_secret_jwt_key
DATABASE_URL=postgresql://postgres:YOUR_POSTGRES_PASSWORD@localhost:5432/task_manager_db
GEMINI_API_KEY=your_google_gemini_api_key

Run database migrations and start the server:
flask db upgrade
python run.py

3. Frontend Setup
cd frontend
npm install
npm start

📡 API Endpoints Overview
Authentication (/api/auth)
POST /register: Create a new user account.

POST /login: Authenticate user and return JWT.

GET /me: Retrieve details of the currently authenticated user.

Tasks (/api/tasks)
GET /: Retrieve all tasks for the logged-in user.

POST /: Create a new task.

DELETE /<id>: Delete a specific task.

POST /<id>/ai-suggest: Trigger Gemini AI to generate a strategy for a specific task.

🧠 Engineering Decisions & AI Integration
To ensure a stable frontend experience, the Gemini AI integration (gemini-2.5-flash) is strictly prompted to return responses in a validated JSON schema. The backend intercepts the raw text, parses the JSON payload to extract priority, reason, and next_step, and saves it to the PostgreSQL database. This prevents AI hallucinations from breaking the React UI component structure.

***

### What's next?
Save this file, and your repository is officially ready. Make sure you don't forget to push this updated README to GitHub along with your final code changes (`git add .`, `git commit -m "Update README"`, `git push`). 

Good luck with recording the video—you are going to crush it! Let me know if you need any advice on what to say in the video.