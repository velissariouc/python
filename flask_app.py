# coding: utf-8
# Η προηγούμενη γραμμή χρειάζεται για τα ελληνικά
from mysite import app, cursor, connection
#from mysite.models import User

from flask import  render_template, request, redirect, url_for


from forms import LoginForm

#app.config.from_object(Config)

# οι παρακατω 4 γραμμες για ελληνικα
import sys
if sys.version_info.major < 3:
    reload(sys)
    sys.setdefaultencoding('utf8')

#app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def arxiki_selida():

    return 'dddd'



#Δημιουργία ιστοσελίδας χρησιμοποιώντας πρότυπο (template)
#To συγκεκριμενο προτυπο χρησιμοποιεί και μια μεταβλητη, την message
@app.route('/test1')
def test1():
    message = "δοκιμη"
    return render_template('welcome.html', message=message)  # render a template

# περναω στο προτυπο πολλες παραμετρους βάζοντάς τες μεσα σε πινακα-λεξικο
# το διπλο αστερακι ** σπάει τον πίνακα σε ξεχωριστες μεταβλητές
@app.route('/test2')
def test2():
    data={}
    data["message"] = "2η δοκιμη"
    data["x"]=5
    return render_template('welcome.html', **data)  # render a template

@app.route('/mesos_oros')
def mesos_oros():
    return render_template('mesos_oros.html')

@app.route('/greek')
def greek_page():
    return '''
    <pre>
<code># coding: utf-8
# Η προηγούμενη γραμμή χρειάζεται για τα ελληνικά

from flask import Flask,  render_template

# οι παρακατω 4 γραμμες για ελληνικα
import sys
if sys.version_info.major < 3:
    reload(sys)
    sys.setdefaultencoding('utf8')</code>
</pre>
<br><br>
<a href="https://www.w3schools.com/python/python_classes.asp">Classes tutorial</a>

<br><br>

<a href="https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms">Flask tutorial</a>
    '''

@app.route('/clients')
def clients_page():
    sql = """SELECT * from CLIENTS"""
    cursor.execute(sql)
    records = cursor.fetchall()
    return  render_template('clients.html',  title='Πελάτες', rows=records)

@app.route('/employees')
def employeess_page():
    sql = """SELECT * from employees"""
    cursor.execute(sql)
    records = cursor.fetchall()
    return  render_template('employees.html',  title='Υπάλληλοι', rows=records)

@app.route('/index')
def index():
    user = {'username': 'Κώστας'}
    posts = [
        {
            'author': {'username': 'Κωστας'},
            'body': 'ωραια μέρα in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/addemployee/', methods=["GET"])
def addemployee_get_page():
    return render_template('addemployee.html',  title='Νεος Υπάλληλος')

@app.route('/addemployee/', methods=["POST"])
def addemployee_post_page():
    first = request.form['first']
    last = request.form['last']
    with connection:
        cursor.execute("INSERT INTO employees (first, last) VALUES (:first, :last)", {'first': first, 'last': last})
    return redirect(url_for('employeess_page'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)