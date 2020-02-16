# coding: utf-8
# Î— Ï€ÏÿÎ¿Î·Î³Î¿ÏÿÎ¼ÎµÎ½Î· Î³ÏÿÎ±Î¼Î¼Î® Ï‡ÏÿÎµÎ¹Î¬Î¶ÎµÏ„Î±Î¹ Î³Î¹Î± Ï„Î± ÎµÎ»Î»Î·Î½Î¹ÎºÎ¬
from flask import Flask
#import os

#basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

import sqlite3

connection = sqlite3.connect('test.db')  # You can create a new database by changing the name within the quotes
cursor = connection.cursor() # The database will be saved in the location where your 'py' file is saved

# Create table - EMPL
cursor.execute('''CREATE TABLE  IF NOT EXISTS employees(
        [ID] INTEGER PRIMARY KEY,
        first text,
        last text,
        pay integer,
        phone text)'''
    )
sql = "SELECT count(*) from employees"
cursor.execute(sql)
records = cursor.fetchall()
record = records[0]
if record[0] == 0:
    sql=''' INSERT INTO employees(first, last, pay) VALUES("Kostas", "Velis", "1000")'''
    cursor.execute(sql)
    sql=''' INSERT INTO employees(first, last, pay) VALUES("Ìáñéá", "Ðåíôáãéþôéóá", "1600")'''
    cursor.execute(sql)
connection.commit()
