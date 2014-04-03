DROP DATABASE College_Scoop;

CREATE DATABASE IF NOT EXISTS College_Scoop;
GRANT ALL PRIVILEGES ON College_Scoop.* to 'blogUser'@'localhost'
identified by 'blogPassword' WITH GRANT OPTION;
USE College_Scoop;

CREATE TABLE IF NOT EXISTS collegescoop_tbl
(
  postername VARCHAR(30),
  activity TEXT,
  rank INT,
);

CREATE TABLE IF NOT EXISTS userscoop_tbl
(
  username VARCHAR(30),
  password VARCHAR(50),
);


