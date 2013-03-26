"""
tipsy.py -- A flask-based todo list
"""

from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", user_name="lauren")

@app.route("/tasks")
def list_tasks():
	db = model.db()
	tasks_from_db = model.get_tasks(db, None)
	return render_template("list_tasks.html", tasks=tasks_from_db)

@app.route("/new_tasks")
def new_tasks():
    return render_template("new_task.html")

@app.route("/save_task", methods=["POST"]) 
def save_task():
    task_title = request.form['task_title']
    db = model.db()
    # Assume that all tasks are attached to user 1.
    task_id = model.new_task(db, task_title, 1)
    return "Success!"


@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/save_user", methods=["POST"]) 
def save_user():
    task_title = request.form['name']
    db = model.db()
    # Assume that all tasks are attached to user 1.
    user_id = model.new_user(db, name, 1)
    return "Success!"

@app.route("/complete_task", methods=["POST"])
def complete_task():
	task_title = request.form['task_title']
	db = model.db()
	return "Task Completed!"


@app.route("/login")
def login():
	return render_template("login.html")
	# db = model.db()

# 	return "Welcome!"


if __name__ == "__main__":
    app.run(debug=True)