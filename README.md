# 🤖 AI Agent App

A lightweight **Flask** web application providing a clean chat interface to **Google Gemini** (`gemini-2.5-flash-lite`). Users can ask any question and get instant AI-generated answers through a simple, self-contained HTML/JS front end.

---

## ✨ Features

- **Single-page chat UI** with a modern gradient design, built entirely in one HTML template (`templates/index.html`) with inline CSS/JS — no build step required.
- **Flask backend API** with two endpoints:
  - `POST /api/set-api-key` — lets a user supply their own Gemini API key at runtime, stored in the Flask session.
  - `POST /api/chat` — sends the user's message to Gemini and returns the AI response.
- **Flexible API key resolution** — uses a session-stored key if provided, otherwise falls back to the `GEMINI_API_KEY` environment variable.
- **Simple, dependency-light stack** — just Flask and the `google-genai` SDK.

---

## 🗂️ Project Structure

```
ai-agent-app/
├── app.py                  # Flask app: routes for home page, API key setting, and chat
├── requirements.txt         # Python dependencies
├── templates/
│   └── index.html           # Chat UI (HTML/CSS/JS, single file)
└── .env                      # API key configuration (not committed)
```

---

## ⚙️ Requirements

- Python 3.9+
- A **Google Gemini API key**

Dependencies (see `requirements.txt`):

```
Flask==3.0.0
google-genai==1.0.0
```

---

## 🔧 Setup

1. **Navigate into the project folder:**
   ```bash
   cd ai-agent-app
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables.** Create a `.env` file in the project root (or export the variable directly):
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   > Alternatively, you can supply an API key at runtime via the `/api/set-api-key` endpoint without setting an environment variable.

---

## ▶️ Usage

Run the Flask development server:

```bash
python app.py
```

The app will be available at:

```
http://localhost:5000
```

Open it in your browser and start chatting — type a question in the input box and press **Send** (or hit Enter).

---

## 🔌 API Reference

### `POST /api/set-api-key`

Sets a Gemini API key for the current browser session.

**Request body:**
```json
{ "api_key": "your_gemini_api_key" }
```

**Response:**
```json
{ "success": true }
```

### `POST /api/chat`

Sends a message to Gemini and returns its response.

**Request body:**
```json
{ "message": "What is artificial intelligence?" }
```

**Response (success):**
```json
{ "success": true, "message": "AI response text..." }
```

**Response (error):**
```json
{ "success": false, "error": "Description of the error" }
```

---

## 🧠 How It Works

1. The Flask app serves a single chat page (`index.html`) with an input box and a message list.
2. On send, the front-end JavaScript posts the user's message to `/api/chat` via `fetch`.
3. The backend retrieves an API key (session-stored or from the environment), creates a `genai.Client`, and calls `generate_content()` with model `gemini-2.5-flash-lite`.
4. The AI's response text is returned as JSON and appended to the chat window.

---

## 🛠️ Tech Stack

| Component      | Technology                          |
|------------------|---------------------------------------|
| Backend           | Flask                                  |
| LLM                | Google Gemini (`gemini-2.5-flash-lite`) |
| Frontend           | Plain HTML/CSS/JavaScript               |
| Session management  | Flask sessions (`app.secret_key`)         |

---

## ⚠️ Notes & Security

- `app.secret_key` is hardcoded as a placeholder string in `app.py` — **replace it with a securely generated secret** before deploying beyond local development.
- API keys entered via `/api/set-api-key` are stored in the Flask session (server-side, cookie-referenced) — do not expose this app publicly without adding proper authentication and HTTPS.
- `debug=True` is enabled in `app.run()` — disable this in any production deployment.

---

## 📄 License

This project is provided as-is for educational and personal use. Add a license of your choice before distributing.
