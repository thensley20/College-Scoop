DROP DATABASE College_Scoop;

CREATE DATABASE IF NOT EXISTS College_Scoop;
GRANT ALL PRIVILEGES ON College_Scoop.* to 'blogUser'@'localhost'
identified by 'blogPassword' WITH GRANT OPTION;
USE College_Scoop;

CREATE TABLE IF NOT EXISTS users
(
  user_id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(30),
  password VARCHAR(50),
  PRIMARY KEY(user_id)
);

CREATE TABLE IF NOT EXISTS club_name
(

  club_id INT NOT NULL AUTO_INCREMENT,
  postername VARCHAR(30),
  PRIMARY KEY(club_id)
  
);

CREATE TABLE IF NOT EXISTS activity
(
  activity_id INT NOT NULL AUTO_INCREMENT,
  activity TEXT,
  rank INT,
  PRIMARY KEY(activity_id)

);


