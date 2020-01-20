# coding: utf-8
# Η προηγούμενη γραμμή χρειάζεται για τα ελληνικά
from flask import Flask
#import os

#basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

import sqlite3

connection = sqlite3.connect('test.db')  # You can create a new database by changing the name within the quotes
cursor = connection.cursor() # The database will be saved in the location where your 'py' file is saved

# Create table - CLIENTS
cursor.execute('''CREATE TABLE  IF NOT EXISTS CLIENTS
             ([ID] INTEGER PRIMARY KEY,[Name] text,  [Date] date)''')
sql = """SELECT count(*) from CLIENTS"""
cursor.execute(sql)
records = cursor.fetchall()
record = records[0]
if record[0] == 0:
    sql=''' INSERT INTO CLIENTS(Name, Date) VALUES("Kostas", "2019-12-15")'''
    cursor.execute(sql)
    sql=''' INSERT INTO CLIENTS(Name, Date) VALUES("ΜΑρία", "2019-12-15")'''
    cursor.execute(sql)
connection.commit()

# Create table - EMPL
cursor.execute('''CREATE TABLE  IF NOT EXISTS employees
             ([ID] INTEGER PRIMARY KEY,first text,
            last text,
            pay integer)''')
sql = """SELECT count(*) from employees"""
cursor.execute(sql)
records = cursor.fetchall()
record = records[0]
if record[0] == 0:
    sql=''' INSERT INTO employees(first, last, pay) VALUES("Kostas", "Velis", "1000")'''
    cursor.execute(sql)
    sql=''' INSERT INTO employees(first, last, pay) VALUES("Μαρια", "Πενταγιώτισα", "1600")'''
    cursor.execute(sql)
connection.commit()

