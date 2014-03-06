DROP DATABASE collegeScoop;

CREATE DATABASE IF NOT EXISTS collegeScoop;
GRANT ALL PRIVILEGES ON collegeScoop.* to 'User'@'localhost' 
identified by 'Password';
USE collegeScoop;

CREATE TABLE scoop
(
  club VARCHAR(50), 
  act BLOB,
  votes int,
);