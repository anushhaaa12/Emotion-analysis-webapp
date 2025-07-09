# Emotion Reflection Tool Backend
This is a simple React + TypeScript frontend for the Emotion Reflection Tool.
## Setup

1. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv venv
   . venv/Scripts/activate  # On Windows
   source venv/bin/activate # On Mac/Linux
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
Start the development server:
   ```
   npm start
   ```

- The app will run at http://localhost:3000
- Make sure the backend FastAPI server is running at http://127.0.0.1:8000
- The frontend will POST to `/analyze` on the backend for emotion analysis.
## Run the server

```sh
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000/analyze`. 
