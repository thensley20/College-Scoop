from flask import Flask, render_template, request , redirect, url_for
import utils
import MySQLdb


app = Flask(__name__)

@app.route('/')
def sindex():

    return render_template('index.html', selectedMenu='Home')


@app.route('/page')
def page():
    return render_template('page.html', selectedMenu='Add')
  
@app.route('/another_page', methods = ['POST'])
def another_page():
  
  
    scoop = {'postername': request.form['postername'],
               'activity': request.form['activity'],
               'rank': request.form['rank']
               }
    
    #cur = db.cursor()
    
    # if user typed in a post ...
    
    if request.method == 'POST':
        db = utils.db_connect()
        cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        query = "INSERT INTO collegescoop_tbl VALUES ('" + request.form['postername'] + "', '" + request.form['activity'] + "', '" + request.form['rank'] + "')"
        # Print query to console (useful for debugging)
        print query
        cur.execute(query)
        db.commit()
        
    cur.execute('select * from collegescoop_tbl')
    rows = cur.fetchall()
	
    return render_template('another_page.html', collegescoop_tbl = rows, scoop = scoop)

  
@app.route('/another_page2', methods=['GET', 'POST'])
def another_page2():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
      
    query = 'SELECT * from collegescoop_tbl'
    
    cur.execute(query)
    rows = cur.fetchall()
    

    cur.execute('select * from collegescoop_tbl')
    rows = cur.fetchall()
  
    
    
    return render_template('another_page2.html', collegescoop_tbl=rows, selectedMenu='List')

	
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)