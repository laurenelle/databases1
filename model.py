"""
model.py
"""

import sqlite3

def connect_db():
	return sqlite3.connect("tipsy.db")


#bob_id = new_user(db, "bob@loblaw.com", "password", "Bob Loblaw")
def new_user(db, email, password, name):
    c = db.cursor()
    query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""
    result = c.execute(query, (email, password, name))
    db.commit()
    return result.lastrowid
    print result.lastrowid

def authenticate(db, email, password):
    c = db.cursor()
    query = """SELECT * FROM Users WHERE email=? AND password=?"""
    c.execute(query, (email, password))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "username"]
        return dict(zip(fields, result))
		#zip returns a list of tuples
	print "Please enter a valid username and password."

def get_user(db, user_id):
	c = db.cursor()
	query = """SELECT * FROM Users WHERE user_name=?"""
	result = c.fetchone()
	if result:
		credentials = ['id', 'email', 'password', 'name']
		return dict(zip(credentials, result))
		#zip returns a list of tuples
	else:
		print "Please enter a valid name and password."

def get_task(db, task_id):
	c = db.cursor()
	query = """SELECT * FROM Tasks WHERE task_id=?"""
	result = c.fetchone()
	if result:
		credentials = ['id', 'title', 'created_at', 'completed_at', 'user_id']
		return dict(zip(credentials, result))
		#zip returns a list of tuples
	return None

def get_tasks(db, user_id):
	c = db.cursor()
	query = """SELECT * FROM Tasks WHERE user_id=?"""
	result = c.fetchone()
	if result:
		user_id = True
		print "USER SPECIFIC TASKS"
		return dict(zip(result))
	return
	query = """SELECT * FROM Tasks"""
	result = c.fetchone()
	print "ALL TASKS"
	return dict(zip(result))


def new_task(db, title, user_id):
	c = db.cursor()
	query = """INSERT INTO Tasks VALUES (NULL, ?, ?)"""
	created_at = NULL #datetime.now()
	completed_at = NULL
	result = c.execute(query, (title, user_id, created_at,
    completed_at))
	db.commit()
	return result.lastrowid
	print result.lastrowid

def complete_task(db, task_id):
	c = db.cursor()
	query = """INSERT INTO Tasks VALUES (?)"""



## new_task(db, title, user_id) 
# -- Created a new task, returns the id of the newly created row. Make sure to populate the created_at field.
## get_user(db, user_id) 
# -- Fetch a user's record based on his id. Return the user as a dictionary, like our authenticate method.
## complete_task(db, task_id)
#  -- Marks a task as being complete, setting the completed_at field.
# get_tasks(db, user_id) 
# -- Gets all the tasks for the given user id. Returns all the tasks in the system if no user_id is given. Returns them as a list of dictionaries.
## get_task(db, task_id)
#  -- Get a single task, given its id. Return the task as a dictionary as above in the authenticate method.




# test with where clause with select and then use UPDATE values
