import sqlite3

# connect to the db

with sqlite3.connect('flaskdb.db') as connection:
	cn = connection.cursor()
	# cn.execute("""DROP TABLE news""")
	cn.execute("""CREATE TABLE news(title TEXT, content TEXT)""")
	cn.execute("INSERT INTO news VALUES('Python', 'Greate programming language to learn and use.')")
	cn.execute("INSERT INTO news VALUES('Django', 'Greate Framework to learn for web development.')")
	cn.execute("INSERT INTO news VALUES('JavaScript', 'Greate programming language nice for front end.')")
	cn.execute("INSERT INTO news VALUES('Postgres', 'Database programming language very good with django.')")


	# cn.execute("""CREATE TABLE companies(name TEXT, cloth TEXT, electronic TEXT, furniture TEXT)""")
	# cn.execute("INSERT INTO news VALUES('Jon Lews', 'Greate programming language to learn and use., ')")
	# cn.execute("INSERT INTO news VALUES('HM', 'Greate Framework to learn for web development.')")
	# cn.execute("INSERT INTO news VALUES('Boss', 'Greate programming language nice for front end.')")
	# cn.execute("INSERT INTO news VALUES('Next', 'Database programming language very good with django.')")
