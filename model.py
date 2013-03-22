"""
model.py
"""

import sqlite3

def connect_db():
	return sqlite3.connect("tipsy.db")

# def new_user(db, email, password, first_name, last_name, user_name):
# 	c = db.cursor()
# 	query = """INSERT INTO Users VALUES (NULL, ?, ?, ?, ?, ?)"""
# 	result = c.execute(query, (email, password, first_name, last_name, user_name)
# 	db.commit()
# 	return result.lastrowid

def new_user(db, email, password, first_name, last_name):
    c = db.cursor()
    query = """INSERT INTO Users VALUES (NULL, ?, ?, ?, ?)"""
    result = c.execute(query, (email, password, first_name, last_name))
    db.commit()
    return result.lastrowid

def authenticate(user_name, password):
	c = db.cursor()
	query = """SELECT * FROM Users WHERE user_name=? AND password=?"""
	result = c.fetchall()
	if result:
		credentials = ['id', 'password', 'first_name', 'last_name', 'user_name']
		return dict(zip(credentials, result))
		#zip returns a list of tuples
	return None

