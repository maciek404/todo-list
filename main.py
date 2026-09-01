from flask import Flask, render_template, redirect, request, url_for
from database import db, Task, Priority, Status
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        priority_str = request.form.get('priority')
        due_date_str = request.form.get('due_date')
        description = request.form.get('description', '').strip()
        if title:
            due_date = date.fromisoformat(due_date_str) if due_date_str else None
            description = description or None
            new_task = Task(
                title=title,
                description=description,
                priority=Priority[priority_str].value,
                due_date=due_date,
            )
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('home'))

    sort_by = request.args.get('sort', 'created_at')
    order = request.args.get('order', 'asc')

    sort_column = getattr(Task, sort_by)
    sort_column = sort_column.desc() if order == 'desc' else sort_column.asc()

    def tasks_by_status(status):
        return Task.query.filter_by(status=status).order_by(sort_column).all()

    return render_template(
        'index.html',
        tasks_todo=tasks_by_status(Status.TODO.value),
        tasks_in_progress=tasks_by_status(Status.IN_PROGRESS.value),
        tasks_done=tasks_by_status(Status.DONE.value),
        sort_by=sort_by,
        order=order,
    )

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    current_taks = db.get_or_404(Task, task_id)
    db.session.delete(current_taks)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    current_task = db.get_or_404(Task, task_id)
    sort_by = request.form.get('sort')
    order = request.form.get('order')
    if request.method == 'POST':
        title = request.form.get('title').strip()
        description = request.form.get('description', '').strip()
        if title:
            priority = request.form.get('priority')
            due_date = request.form.get('due_date')
            current_task.title = title
            current_task.description = description or None
            current_task.priority = Priority[priority].value
            current_task.due_date = date.fromisoformat(due_date) if due_date else None
            db.session.commit()
            return redirect(url_for('home', sort=sort_by, order=order))
    sort_by = request.args.get('sort', 'created_at')
    order = request.args.get('order', 'asc')
    return render_template('edit.html', task=current_task, sort=sort_by, order=order)

@app.route('/move/<int:task_id>/<string:direction>', methods=['POST'])
def move_task(task_id, direction):
    sort_by = request.args.get('sort', 'created_at')
    order = request.args.get('order', 'asc')
    current_task = db.get_or_404(Task, task_id)
    if direction == 'next' and current_task.status != Status.DONE.value:
        current_task.status += 1
        db.session.commit()
    elif direction == 'prev' and current_task.status != Status.TODO.value:
        current_task.status -= 1
        db.session.commit()
    return redirect(url_for('home', sort=sort_by, order=order))

if __name__ == '__main__':
    app.run(debug=True)