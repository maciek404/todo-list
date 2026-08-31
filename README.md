# To-Do List App

A full-featured to-do list web application built with Flask and styled with Tailwind CSS. Users can create, edit, complete, and delete tasks, each with a priority level and an optional due date. Tasks can be filtered by status and sorted by creation date, due date, or priority.

## Features

- Create, edit, and delete tasks
- Mark tasks as done / not done
- Assign a priority to each task (Low, Medium, High)
- Optional due date per task
- Filter tasks by status (All / Active / Done)
- Sort tasks by creation date, due date, or priority, in ascending or descending order
- Clean, responsive UI built with Tailwind CSS

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite, accessed via Flask-SQLAlchemy (SQLAlchemy ORM)
- **Templating:** Jinja2
- **Styling:** Tailwind CSS (compiled via the Tailwind CLI)
- **Frontend:** Server-rendered HTML with plain forms (no JavaScript framework)

## Project Structure

```
.
├── main.py                  # Flask app, routes
├── database.py               # SQLAlchemy models (Task, Priority)
├── requirements.txt           # Python dependencies
├── package.json               # Node dependencies (Tailwind CSS)
├── static/
│   └── css/
│       ├── input.css          # Tailwind entry file
│       └── output.css         # Compiled CSS (committed for convenience)
└── templates/
    ├── index.html              # Task list, add form, filters, sorting
    └── edit.html                # Edit form for an existing task
```

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js and npm (only required if you want to rebuild the CSS; the compiled `output.css` is already included in the repository)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/maciek404/todo-list.git
   cd your-repo-name
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the app:
   ```
   python main.py
   ```

5. Open your browser at `http://localhost:5000`

The database file is created automatically on first run.

### Rebuilding the CSS (optional)

The compiled Tailwind CSS file is already included in the repository, so the app will display correctly without any additional steps. If you want to modify the styling, you will need Node.js installed:

```
npm install
npx @tailwindcss/cli -i ./static/css/input.css -o ./static/css/output.css --watch
```

## Data Model

Each task has the following fields:

- `title` — the task description
- `is_done` — completion status
- `priority` — Low, Medium, or High
- `due_date` — optional due date
- `created_at` — timestamp set automatically when the task is created

## Notes

This project was built as a learning exercise, following a classic Flask request/response cycle (form submissions with page reloads, no AJAX). It intentionally uses plain HTML forms instead of Flask-WTF to focus on core request handling and form validation fundamentals.
