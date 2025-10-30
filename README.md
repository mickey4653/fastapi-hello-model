# Hello Model – Week 1 fastapi-hello-model

Simple FastAPI project to get comfortable with Python backend basics.

### ✅ Features
- **GET /**: Health/greeting endpoint
- **POST /echo**: Echoes back a sent message using a Pydantic model

### 📦 Requirements
- Python 3.10+ recommended
- See `requirements.txt`:
  - `fastapi==0.115.0`
  - `uvicorn==0.30.0`
  - `requests==2.32.3`

### 🚀 Run Locally
```bash
# (Optional) Create & activate a virtual environment
python -m venv venv
# Windows (Git Bash / PowerShell):
source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --reload
```

- App will be available at `http://127.0.0.1:8000`
- Interactive docs (Swagger): `http://127.0.0.1:8000/docs`
- Alternative docs (ReDoc): `http://127.0.0.1:8000/redoc`

### 🔌 API Endpoints

- **GET /**  
  Response:
  ```json
  { "message": "Welcome to your first AI API 🚀" }
  ```

- **POST /echo**  
  Request body:
  ```json
  { "text": "Hello" }
  ```
  Response:
  ```json
  { "your_message": "Hello" }
  ```

### 🧪 Curl Examples
```bash
# GET /
curl http://127.0.0.1:8000/

# POST /echo
curl -X POST http://127.0.0.1:8000/echo \
  -H "Content-Type: application/json" \
  -d '{"text":"Hello FastAPI"}'
```

### 🗂️ Project Structure
```
.
├─ app/
│  ├─ __init__.py
│  └─ main.py
├─ requirements.txt
└─ README.md
```


