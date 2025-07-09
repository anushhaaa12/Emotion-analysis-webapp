# Emotion Reflection Tool Backend

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

## Run the server

```sh
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000/analyze`. 