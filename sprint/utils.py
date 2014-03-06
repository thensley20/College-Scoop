import MySQLdb


DATABASE='collegeScoop'
DB_USER = 'User'
DB_PASSWORD = 'Password'
HOST = 'localhost'

def db_connect():
  return MySQLdb.connect(HOST, DB_USER, DB_PASSWORD, DATABASE)