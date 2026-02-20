# Task Manager App — AngularJS + Flask REST API

A full-stack Task Manager application built with **AngularJS** (frontend) and **Flask** (backend REST API) backed by **SQLite (RDBMS)**. Includes unit and integration tests.

## Tech Stack

| Layer     | Technology                  |
|-----------|-----------------------------|
| Frontend  | AngularJS 1.8, HTML, CSS    |
| Backend   | Python, Flask, Flask-CORS   |
| Database  | SQLite (RDBMS)              |
| Testing   | Python unittest             |

## Features

- Create, Read, Update, Delete (CRUD) tasks
- Filter tasks by status: Pending / In Progress / Completed
- RESTful API with proper HTTP status codes
- Unit & Integration test coverage for all endpoints

## Project Structure

```
task-manager/
├── backend/
│   ├── app.py              # Flask REST API
│   └── requirements.txt
├── frontend/
│   └── index.html          # AngularJS single-page app
└── tests/
    └── test_app.py         # Unit & Integration tests
```

## Setup & Run

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
# API runs at http://localhost:5000
```

### Frontend

Open `frontend/index.html` in your browser (backend must be running).

### Run Tests

```bash
cd tests
python -m pytest test_app.py -v
```

## API Endpoints

| Method | Endpoint           | Description        |
|--------|--------------------|--------------------|
| GET    | /api/tasks         | Get all tasks      |
| GET    | /api/tasks/:id     | Get task by ID     |
| POST   | /api/tasks         | Create a new task  |
| PUT    | /api/tasks/:id     | Update a task      |
| DELETE | /api/tasks/:id     | Delete a task      |

## Author

**Vaddi Ranga Koushik**  
GitHub: [Bunny0311](https://github.com/Bunny0311)  
LinkedIn: [koushik-vaddi-ranga](https://www.linkedin.com/in/koushik-vaddi-ranga-b958962a8/)
