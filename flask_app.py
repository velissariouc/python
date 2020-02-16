# coding: utf-8
# A very simple Flask Hello World app for you to get started with...

from mysite import cursor, connection, app, readTable
from flask import Flask, render_template, flash, redirect, request, url_for

# οι παρακατω 4 γραμμες για ελληνικα
import sys
if sys.version_info.major < 3:
    reload(sys)
    sys.setdefaultencoding('utf8')

@app.route('/')
def first_page():
    return redirect(url_for('employeess_page'))

@app.route('/employees')
def employeess_page():
    sql = """SELECT * from employees"""
    cursor.execute(sql)
    records = cursor.fetchall()
    return  render_template('employees.html',  title='Υπάλληλοι', rows=records)

@app.route('/addemployee/', methods=["GET"])
def addemployee_get_page():
    return render_template('addemployee.html',  title='Νέος Υπάλληλος')

@app.route('/addemployee/', methods=["POST"])
def addemployee_post_page():
    first = request.form['first']
    last = request.form['last']
    salary = request.form['salary']
    phone = request.form['phone']
    with connection:
        cursor.execute("INSERT INTO employees (first, last, pay,phone) VALUES (:first, :last, :salary, :phone)",
        {'first': first, 'last': last, 'salary': salary, 'phone': phone})
    return redirect(url_for('employeess_page'))

@app.route('/deleteemployee')
def deleteemployee():
    ID = request.args.get('ID')
    with connection:
        cursor.execute("delete from employees where ID=" + ID )
    return redirect(url_for('employeess_page'))
