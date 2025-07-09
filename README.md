# Emotion Reflection Tool

A simple web app for reflecting on your emotions. Enter a short text reflection, and the app will return a mock emotion analysis.

## Project Structure
- `frontend/` — React + TypeScript frontend
- `backend/` — FastAPI Python backend

---

## Setup Instructions

### 1. Backend (API)

1. Open a terminal and navigate to the `backend` folder:
   ```
   cd backend
   ```
2. (Optional) Activate your virtual environment:
   ```
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the API server:
   ```
   uvicorn main:app --reload
   ```
   The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 2. Frontend (Web App)

1. Open a new terminal and navigate to the `frontend` folder:
   ```
   cd frontend
   ```
2. Install dependencies:
   ```
   npm install
   ```
3. Start the development server:
   ```
   npm start
   ```
   The app will run at [http://localhost:3000](http://localhost:3000)

---

## Usage
- Enter a reflection in the web app and submit.
- The backend will return a random emotion and confidence score (mock analysis).

---

## Notes
- The emotion analysis is random and for demonstration only.
- Make sure both servers are running at the same time for full functionality. 