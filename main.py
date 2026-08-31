from flask import Flask, render_template, redirect, request, url_for
from database import db, Task, Priority
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form.get('title').strip()
        priority_str = request.form.get('priority')
        due_date_str = request.form.get('due_date')
        if title:
            due_date = date.fromisoformat(due_date_str) if due_date_str else None
            new_task = Task(
                title=title,
                priority=Priority[priority_str].value,
                due_date=due_date,
            )
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('home'))

    status_filter = request.args.get('status', 'all')
    sort_by = request.args.get('sort', 'created_at')
    order = request.args.get('order', 'asc')

    query = Task.query
    if status_filter == 'active':
        query = query.filter_by(is_done=False)
    elif status_filter == 'done':
        query = query.filter_by(is_done=True)

    sort_column = getattr(Task, sort_by)
    sort_column = sort_column.desc() if order == 'desc' else sort_column.asc()
    query = query.order_by(sort_column)
    tasks = query.all()
    return render_template(
        'index.html',
        tasks=tasks,
        sort_by=sort_by,
        order=order,
        status_filter=status_filter,
    )

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    current_task = db.get_or_404(Task, task_id)
    current_task.is_done = not current_task.is_done
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    current_taks = db.get_or_404(Task, task_id)
    db.session.delete(current_taks)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    current_task = db.get_or_404(Task, task_id)
    if request.method == 'POST':
        title = request.form.get('title').strip()
        if title:
            priority = request.form.get('priority')
            due_date = request.form.get('due_date')
            current_task.title = title
            current_task.priority = Priority[priority].value
            current_task.due_date = date.fromisoformat(due_date) if due_date else None
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('edit.html', task=current_task)

if __name__ == '__main__':
    app.run(debug=True)