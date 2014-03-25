from flask import Flask, render_template, request , redirect, url_for
import utils
import MySQLdb


app = Flask(__name__)

@app.route('/', methods =['GET','POST'])
def sindex():
    
    return render_template('index.html', selectedMenu='Home')


@app.route('/page')
def page():
    return render_template('page.html', selectedMenu='Add')
  
@app.route('/another_page', methods = ['GET','POST'])
def another_page():
  
    print('anotherpage')
    scoop = {'postername': MySQLdb.escape_string(request.form['postername']),
               'activity': MySQLdb.escape_string(request.form['activity']),
               'rank': request.form['rank']
             
               }
    
    if request.method == 'POST':
        db = utils.db_connect()
        cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        
        query = "INSERT INTO club_name (postername) VALUES ('" + MySQLdb.escape_string(request.form['postername']) + "')"
        # Print query to console (useful for debugging)
        print query
        cur.execute(query)
        #db.commit()
        
        query2 = "INSERT INTO activity (activity, rank) VALUES ('" + MySQLdb.escape_string(request.form['activity']) + "', '" + request.form['rank'] + "')"
        # Print query to console (useful for debugging)
        print query2
        cur.execute(query2)
        db.commit()
        
        
    cur.execute('SELECT DISTINCT cn.postername, a.activity, a.rank FROM club_name cn JOIN activity a')
    rows = cur.fetchall()

    return render_template('another_page.html', club_name=rows, activity = rows, scoop = scoop)

  
@app.route('/another_page2', methods=['GET', 'POST'])
def another_page2():
    # add code snippet that adds either one or -1 to rank of club. also check to see if user has voted
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
      
    query = 'SELECT DISTINCT cn.postername, a.activity, a.rank FROM club_name cn JOIN activity a'
    
    cur.execute(query)
    rows = cur.fetchall()
    

    #cur.execute('SELECT cn.postername, a.activity, a.rank FROM club_name cn JOIN activity a')
    #rows = cur.fetchall()
  
    
    
    return render_template('another_page2.html', club_name=rows, activity=rows, selectedMenu='List')

@app.route('/login', methods = ['GET','POST'])
def login():
  #check with db to see if user is registered in userscoop_tbl, push session if user is in db else prompt login was failed
  
    return render_template('login.html')

@app.route('/logout', methods = ['GET','POST'])
def logout():
  #session pop
    return render_template('logout.html')

@app.route('/register')
def register():
    #method to insert username and password into userscoot_tbl
    #if post it runs insert then renders login for user to enter website
    if request.method == 'POST':
        db = utils.db_connect()
        cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        query = "INSERT INTO users (username, password) VALUES ('" + MySQLdb.escape_string(request.form['ruser']) + "', '" + MySQLdb.escape_string(request.form['rpass']) + "')"
        # Print query to console (useful for debugging)
        print query
        cur.execute(query)
        db.commit()
        return render_template('login.html')
    return render_template('register.html')
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)