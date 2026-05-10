SELECT first_name, last_name FROM students;

SELECT email FROM students ORDER BY email;

SELECT first_name, last_name, gpa FROM students WHERE gpa > 3.5;

SELECT * FROM students WHERE enrollment_year = 2021;

SELECT first_name, last_name, gpa FROM students WHERE gpa BETWEEN 3.0 AND 3.5;

SELECT * FROM students WHERE email = 'grace@school.edu';

SELECT * FROM students ORDER BY id LIMIT 5;

SELECT * FROM students WHERE gpa IS NULL;

SELECT first_name, last_name, salary FROM teachers WHERE salary > 80000;

SELECT code, title FROM courses WHERE credits = 4;
