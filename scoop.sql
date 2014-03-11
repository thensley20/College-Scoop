DROP DATABASE College_Scoop;

CREATE DATABASE IF NOT EXISTS College_Scoop;
GRANT ALL PRIVILEGES ON College_Scoop.* to 'blogUser'@'localhost' 
identified by 'blogPassword';
USE College_Scoop;

CREATE TABLE collegescoop_tbl
(
  postername VARCHAR(30),
  activity TEXT,
  rank INT,

);