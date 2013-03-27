"""
tipsy.py -- A flask-based todo list
"""

from flask import Flask, render_template, request, redirect, session, escape, url_for, g, flash
import model

app = Flask(__name__)
# set the secret key.  keep this really secret:
app.secret_key = 'a;lskjfieasdlknfweidsksldk'

@app.before_request
def set_up_db():
    g.db = model.db()

@app.teardown_request
def disconnect_db(e):
    g.db.close()

@app.route("/")
def index():
    # if "name" in session:
    # 	session["name"] = request.form["name"]
    	return render_template("index.html")
    # print "You're not logged in yet."
    # return redirect(url_for("login.html"))


# receiving the login credentials
@app.route("/authenticate", methods=["POST"])
def authenticate():
    email = request.form['email']
    password = request.form['password']
    user_id = model.authenticate(g.db, email, password)
    session['user_id'] = user_id
    return redirect("/tasks")#FIX REDIRECT


@app.route("/login", methods=["GET", "POST"])
def login():
	request.method == "POST"
	return render_template("login.html")
	# db = model.db()

# 	return "Welcome!"

@app.route("/task/<int:id>", methods=["GET"])
def view_task(id):
    db = model.db()
    task_from_db = model.get_task(g.db, id)
    return render_template("view_task.html", task=task_from_db)

@app.route("/task/<int:id>", methods=["POST"])
def complete_task(id):
    db = model.db()
    model.complete_task(db, id)
    return redirect("/tasks")

@app.route("/tasks")
def list_tasks():
    db = model.db()
    user_id = session.get("user_id", None)
    tasks_from_db = model.get_tasks(db, user_id)
    return render_template("list_tasks.html", tasks=tasks_from_db)


@app.route("/users")
def list_users():
    db = model.db()
    user_id = session.get("user_id", None)
    users_from_db = model.get_users(db, id)
    return render_template("list_users.html", users=users_from_db)



@app.route("/new_tasks")
def new_tasks():
    return render_template("new_task.html")

@app.route("/save_task", methods=["POST"]) 
def save_task():
    db = model.db()
    task_title = request.form['task_title']
    # Assume that all tasks are attached to user 1.
    task_id = model.new_task(db, task_title, 1)
    return "Success!"


# @app.route("/complete_task", methods=["POST"])
# def complete_task():
# 	db = model.db()
# 	task_title = request.form['task_title']
# 	return "Task Completed!"


@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/save_user", methods=["POST"]) 
def save_user():
    db = model.db()
    user = request.form['name']
    # Assume that all tasks are attached to user 1.
    user_id = model.name(db, name, None)
    return "Success!"

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for("logout.html"))







if __name__ == "__main__":
    app.run(debug=True)