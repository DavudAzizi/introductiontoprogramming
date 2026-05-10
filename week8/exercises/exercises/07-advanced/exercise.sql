CREATE INDEX idx_students_gpa ON students(gpa);

EXPLAIN QUERY PLAN
SELECT * FROM students WHERE gpa > 3.5;

CREATE VIEW enrollment_details AS
SELECT
    s.first_name || ' ' || s.last_name AS student_name,
    c.code,
    c.title,
    g.letter_grade
FROM enrollments e
JOIN students s ON e.student_id = s.id
JOIN courses c ON e.course_id = c.id
LEFT JOIN grades g ON g.enrollment_id = e.id;

SELECT * FROM enrollment_details WHERE letter_grade = 'A';

CREATE VIEW course_statistics AS
SELECT
    c.code,
    c.title,
    COUNT(e.id) AS enrolled_students,
    ROUND(AVG(g.final), 1) AS average_final
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
LEFT JOIN grades g ON g.enrollment_id = e.id
GROUP BY c.id;

INSERT INTO students (first_name, last_name, email, enrollment_year, gpa)
VALUES ('Davud', 'Azizi', 'newstudent@school.edu', 2024, NULL);

SELECT * FROM students WHERE email = 'newstudent@school.edu';

UPDATE students
SET gpa = 3.22
WHERE id = 17;

SELECT *
FROM grades
WHERE letter_grade = 'F';

DELETE FROM grades
WHERE letter_grade = 'F';

BEGIN TRANSACTION;

INSERT INTO enrollments (student_id, course_id)
VALUES (1, 13);

INSERT INTO grades (enrollment_id, midterm, final, letter_grade)
VALUES (last_insert_rowid(), NULL, NULL, NULL);

COMMIT;

BEGIN TRANSACTION;

UPDATE books
SET available_copies = available_copies - 1
WHERE id = 3 AND available_copies > 0;

INSERT INTO loans (member_id, book_id, loan_date, due_date)
SELECT 3, 3, DATE('now'), DATE('now', '+14 days')
WHERE EXISTS (
    SELECT 1 FROM books WHERE id = 3 AND available_copies >= 0
);

COMMIT;

CREATE INDEX idx_students_email ON students(email);

EXPLAIN QUERY PLAN
SELECT * FROM students WHERE LOWER(email) = 'alice@school.edu';

EXPLAIN QUERY PLAN
SELECT * FROM students WHERE email = 'alice@school.edu';

-- Version A is slower because LOWER(email) applies a function to the column,
-- so SQLite cannot use the normal email index efficiently.
-- Version B compares the indexed column directly.

CREATE INDEX idx_enrollments_student_course
ON enrollments(student_id, course_id);

EXPLAIN QUERY PLAN
SELECT * FROM enrollments WHERE student_id = 5 AND course_id = 1;
