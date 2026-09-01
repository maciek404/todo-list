# To-Do List App

A Kanban-style to-do list web application built with Flask and styled with Tailwind CSS. Tasks are organized into three columns — To Do, In Progress, and Done — and can be created, edited, moved between columns, and deleted. Each task can have a priority, an optional due date, and an optional description.

## Features

- Create, edit, and delete tasks
- Three-column board layout: To Do / In Progress / Done
- Move tasks forward or backward between columns, with boundary checks (a task in To Do can only move forward, a task in Done can only move back)
- Assign a priority to each task (Low, Medium, High), shown as a color-coded badge
- Optional due date per task
- Optional description, shown as a truncated two-line preview on the card and in full on the edit form
- Sort tasks by creation date, due date, or priority, in ascending or descending order — the chosen sort is preserved across moving, editing, and navigating back to the board
- Responsive layout: columns stack vertically on small screens and sit side by side on larger ones
- Clean UI built with Tailwind CSS and a custom heading font

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite, accessed via Flask-SQLAlchemy (SQLAlchemy ORM)
- **Templating:** Jinja2, with a reusable macro for task cards
- **Styling:** Tailwind CSS v4 (compiled via the Tailwind CLI), Google Fonts (Space Grotesk)
- **Frontend:** Server-rendered HTML with plain forms (no JavaScript framework, no Flask-WTF)

## Project Structure

```
.
├── main.py                    # Flask app, routes
├── database.py                 # SQLAlchemy models (Task, Priority, Status)
├── requirements.txt             # Python dependencies
├── package.json                 # Node dependencies (Tailwind CSS)
├── static/
│   └── css/
│       ├── input.css            # Tailwind entry file
│       └── output.css           # Compiled CSS (committed for convenience)
└── templates/
    ├── index.html                # Board view: add form, sorting, three columns
    ├── edit.html                 # Edit form for an existing task
    └── _task_card.html            # Reusable task card macro
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

- `title` — the task description (required)
- `description` — optional, longer free-text notes
- `status` — To Do, In Progress, or Done, stored as an integer so the columns and any status-based sorting behave predictably
- `priority` — Low, Medium, or High, also stored as an integer so it sorts by importance rather than alphabetically
- `due_date` — optional due date
- `created_at` — timestamp set automatically when the task is created

## Notes

This project was built as a learning exercise, following a classic Flask request/response cycle (form submissions with page reloads, no AJAX). It intentionally uses plain HTML forms instead of Flask-WTF, and a hand-rolled board layout instead of a JavaScript drag-and-drop library, to focus on core request handling, template composition, and state management (such as preserving the active sort order across page redirects) using only server-rendered HTML.
