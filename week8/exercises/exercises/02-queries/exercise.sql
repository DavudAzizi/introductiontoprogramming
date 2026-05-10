SELECT * FROM students WHERE last_name LIKE '%s%';

SELECT * FROM teachers WHERE email LIKE '%@cs50.harvard.edu';

SELECT first_name, last_name, gpa FROM students ORDER BY gpa DESC LIMIT 5;

SELECT DISTINCT enrollment_year FROM students ORDER BY enrollment_year;

SELECT * FROM courses WHERE department_id IN (1, 2);

SELECT * FROM students WHERE enrollment_year NOT IN (2018);

SELECT * FROM courses ORDER BY credits DESC, title ASC;

SELECT * FROM books WHERE title LIKE 'The%';

SELECT id, member_id, due_date FROM loans WHERE return_date IS NULL;

SELECT * FROM authors WHERE nationality = 'British' ORDER BY last_name;

SELECT * FROM members WHERE membership_type IN ('premium', 'student');

SELECT * FROM students WHERE first_name LIKE '____';
