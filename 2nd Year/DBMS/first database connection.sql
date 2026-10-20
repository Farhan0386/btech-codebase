CREATE DATABASE dbms_practice;
USE dbms_practice;

CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    course VARCHAR(50)
);

INSERT INTO Student
VALUES (1, 'Farhan', 'CSE');

SELECT * FROM Student;