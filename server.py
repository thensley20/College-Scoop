from flask import Flask, session, render_template, request , redirect, url_for
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
        id=cur.lastrowid
        #db.commit()
        
        query2 = "INSERT INTO activity (club_id, activity, rank) VALUES (" + str(id) + ", '" + MySQLdb.escape_string(request.form['activity']) + "', '" + request.form['rank'] + "')"
        # Print query to console (useful for debugging)
        print query2
        cur.execute(query2)
        db.commit()
        
        
    cur.execute('SELECT DISTINCT cn.postername, a.activity, a.rank FROM club_name cn NATURAL JOIN activity a')
    rows = cur.fetchall()

    return render_template('another_page.html', club_name=rows, activity = rows, scoop = scoop)

  
@app.route('/another_page2', methods=['GET', 'POST'])
def another_page2():
    # add code snippet that adds either one or -1 to rank of club. also check to see if user has voted
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
      
    query = 'SELECT DISTINCT cn.postername, a.activity, a.rank FROM club_name cn NATURAL JOIN activity a'
    
    cur.execute(query)
    rows = cur.fetchall()
    

    #cur.execute('SELECT cn.postername, a.activity, a.rank FROM club_name cn JOIN activity a')
    #rows = cur.fetchall()
  
    
    
    return render_template('another_page2.html', club_name=rows, activity=rows, selectedMenu='List')

@app.route('/login', methods = ['GET','POST'])
def login():
  #check with db to see if user is registered in userscoop_tbl, push session if user is in db else prompt login was failed
    global currentUser, success
    
    # if user typed in a post ...
    if request.method == 'POST':
      
        db = utils.db_connect()
        cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        username = request.form['username']
        password = request.form['password']
        query = "SELECT username FROM users WHERE username = '%s' AND password = SHA2('%s',0);"%(username,password)
        print query
        cur.execute(query)
      
        result = cur.fetchone()
        if result is not None:
            return render_template('index.html')
    
    return render_template('login.html')

@app.route('/logout', methods = ['GET','POST'])
def logout():
  #session pop
    return render_template('logout.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    #method to insert username and password into userscoot_tbl
    #if post it runs insert then renders login for user to enter website
    print "Blah"
    if request.method == 'POST':
        db = utils.db_connect()
        cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        query = "INSERT INTO users (username, password) VALUES ('" + MySQLdb.escape_string(request.form['ruser']) + "', SHA2(' " + MySQLdb.escape_string(request.form['rpass']) + "' , 0))"
        # Print query to console (useful for debugging)
        print query
        cur.execute(query)
        db.commit()
        
        return render_template('login.html')
    return render_template('register.html')
  
@app.route('/search', methods=['GET', 'POST'])
def search():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    queryType = 'None'
    #query = "SELECT DISTINCT cn.postername, a.activity, a.rank FROM club_name cn NATURAL JOIN activity a"
    rows = []
    # if user typed in a post ...
    if request.method == 'POST':
      # use for all user input
      searchTerm = MySQLdb.escape_string(request.form['search'])
      if searchTerm == 'clubs':
           query = 'SELECT DISTINCT cn.postername, a.activity, a.rank FROM club_name cn NATURAL JOIN activity a'
           queryType = 'clubs'
      else:
        query = 'SELECT DISTINCT cn.postername, a.activity, a.rank FROM club_name cn NATURAL JOIN activity a WHERE cn.postername LIKE "%%%s%%"' % (searchTerm)
        queryType = 'names'
        print (query)
    
      cur.execute(query)
      rows = cur.fetchall()
      
    
    return render_template('search.html', queryType=queryType, results=rows, selectedMenu='Search')
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)