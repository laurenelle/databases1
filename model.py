
"""
model.py
"""

import sqlite3
import datetime

def db():
	return sqlite3.connect("tipsy.db")


#new_user(db, "bob@loblaw.com", "password", "Bob Loblaw")
def new_user(db, email, password, name):
    c = db.cursor()
    query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""
    result = c.execute(query, (email, password, name))
    db.commit()
    return result.lastrowid

def make_user(row):
    fields = ["id", "email", "password", "username"]
    return dict(zip(fields, row))

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
	query = """SELECT * FROM Users WHERE id=?"""
	c.execute(query, [user_id])
	result = c.fetchone()
	print result
	if result:
		credentials = ['id', 'email', 'password', 'name']
		return dict(zip(credentials, result))
		#zip returns a list of tuples
	else:
		print "Please enter a valid name and password."

def get_task(db, task_id):
	c = db.cursor()
	query = """SELECT * FROM Tasks WHERE id=?"""
	c.execute(query, [task_id])
	result = c.fetchone()
	print result
	if result:
		credentials = ['id', 'title', 'created_at', 'completed_at', 'user_id']
		return dict(zip(credentials, result))
		#zip returns a list of tuples
	return None

def get_tasks(db, user_id = None):
	c = db.cursor()
	query = """SELECT * FROM Tasks WHERE user_id=?"""
	c.execute(query, [user_id])
	result = c.fetchall()
	if result:
		user_id = True
		print "true" 
		print result
	else:
		user_id = None
		query = """SELECT * FROM Tasks"""
		c.execute(query, [])
		result = c.fetchall()
		tasks_list = []
		result = list(result)
		# move into its own function and consider consolidating like line 52,53
		for i, values in enumerate(result):
			each_dict = {
			"id": values[0],
			"title": values[1],
			"created_at": values[2],
			"completed_at": values [3],
			"user_id": values [4]
			}
			tasks_list.append(each_dict)
		return tasks_list


def get_tasks(db, user_id):
    c = db.cursor()
    if user_id:
        query = """SELECT * from Tasks WHERE user_id = ?"""
        c.execute(query, (user_id,))
    else:
        query = """SELECT * from Tasks"""
        c.execute(query)
    tasks = []
    rows = c.fetchall()
    for row in rows:
        task = dict(zip(["id", "title", "created_at", "completed_at", "user_id"], row))
        tasks.append(task)

    return tasks

def new_task(db, title, user_id):
	c = db.cursor()
	query = """INSERT INTO Tasks VALUES (NULL, ?, ?, ?, ?)"""
	created_at = datetime.datetime.now()
	completed_at = None
	result = c.execute(query, (title, created_at,
    completed_at, user_id))
	db.commit()
	return result.lastrowid

def make_task(row):
    fields = ["title", "user_id", "created_at", "completed_at"]
    return dict(zip(fields, row))

def completed_task(db, task_id):
	c = db.cursor()
	query = """UPDATE Tasks SET completed_at = ? WHERE id =?"""
	# only query needs proper column name
	# function variables can be whatever
	completed_at = datetime.datetime.now()
	print completed_at
	result = c.execute(query,(completed_at, task_id))
	# execute method requires a list object (tuple or list)
	db.commit()
	return result.lastrowid



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
