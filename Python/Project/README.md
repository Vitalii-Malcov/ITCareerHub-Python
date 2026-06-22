# Flask Login App

A minimal Flask web application with login form, protected dashboard, and Bootstrap 5 UI.

Built as a learning project to practice Python backend development with Flask and Jinja2.

---

## Features

- Login form with email + password validation
- Protected dashboard showing the logged-in user
- Error messages rendered inside the form (no redirect on failure)
- About page with custom styling
- Bootstrap 5 responsive layout
- Jinja2 templating

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11+ | Core language |
| Flask 3.x | Web framework |
| Jinja2 | HTML templating |
| Bootstrap 5 | Frontend UI |

---

## Installation

```bash
git clone https://github.com/vitalii-malcov/flask-login-app.git
cd flask-login-app

python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
python app.py
```

Then open: http://127.0.0.1:5000

---

## Demo Credentials

> Credentials are hardcoded for demo purposes only.

| Field | Value |
|-------|-------|
| Email | `admin@mail.com` |
| Password | `1234` |

---

## Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Login form |
| GET | `/about` | About page |
| POST | `/login` | Authenticate user |
| GET | `/dashboard` | User dashboard (after login) |

---

## Project Structure

```
flask-login-app/
├── app.py              # Flask application
├── requirements.txt    # Dependencies
└── templates/
    ├── index.html      # Login page
    ├── dashboard.html  # User dashboard
    └── about.html      # About page
```

---

## License

MIT — free to use and modify.