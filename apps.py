from flask import (
	Flask,
	flash,
	g,
	render_template,
	redirect,
	request,
	session, 
	url_for
) 
from functools import wraps
import sqlite3 


app = Flask(__name__)

app.secret_key = 'hello flask'
app.database = 'flaskdb.db'



# login required decorator
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap

@app.route('/')
@login_required
def home():
	# g is an object used in flask that the user has been loggedin
	g.db = connect_db()
	cur = g.db.execute('select * from news')
	# print(cur, '<<')
	# print(cur.fetchall, '>>>')
	# news_dict = {}
	news = []
	for row in cur.fetchall():
		news.append(dict(title = row[0], content = row[1]))
	# 	news_dict['title'] = row[0]
	# 	news_dict['content'] = row[1]
	# 	news.append(news_dict)
	# 	print(news)
	# news = [dict(title=row[0], content=row[1]) for row in cur.fetchall()]
	print(news)
	g.db.close()
	return render_template('index.html', news=news)


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'dilmac' or request.form['password'] != 'admin123':
			error = 'Wrong login details, please try again'
		else:
			session['logged_in'] = True
			flash('You were just logged in!')
			return redirect(url_for('home'))

	return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You were just logged out!')
	return redirect(url_for('home'))


# create a function to connect the database sqlite3
def connect_db():
	return sqlite3.connect(app.database)




if __name__ == '__main__':
	app.run(debug=True)
