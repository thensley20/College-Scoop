from flask import Flask, render_template, request, redirect, url_for
import MySQLdb
import utils

app = Flask(__name__)

@app.route('/another_page2', methods = ['post'])
def another_page():
	#if user posts then we proceed
	if methods == 'post':
		var1= 0 #variable set to zero to initialize votes
		
		#connect to db, make a cursor, and then submit a query to db
		db = utils.db_connect()
    	cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		query = "INSERT INTO scoop VALUES ('" + request.form['username'] + "', '" + request.form['activity']+ "','" + var1)"
		
		#print the query
		print query
        
		
		cur.execute(query)
        db.commit()
		cur.execute('select * from scoop')
		rows = cur.fetchall()
	
	return render_template('another_page.html', posts = rows)

	
@app.route('/another_page')
def another_page():
	return render_template('another_page.html')

@app.route('/')
def sindex():
	return render_template('page.html')
	
@app.route('/page')
def page():
	return render_template('page.html')
	
if __name__ == '__main__':
	app.run(debug = True)