SELECT s.first_name, s.last_name, c.title
FROM enrollments e
JOIN students s ON e.student_id = s.id
JOIN courses c ON e.course_id = c.id;

SELECT c.title, t.first_name, t.last_name
FROM courses c
JOIN teachers t ON c.teacher_id = t.id;

SELECT t.first_name, t.last_name, d.name
FROM teachers t
JOIN departments d ON t.department_id = d.id;

SELECT s.first_name, s.last_name, c.title, t.first_name, t.last_name, g.letter_grade
FROM enrollments e
JOIN students s ON e.student_id = s.id
JOIN courses c ON e.course_id = c.id
JOIN teachers t ON c.teacher_id = t.id
JOIN grades g ON g.enrollment_id = e.id;

SELECT s.*
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
WHERE e.id IS NULL;

SELECT c.*
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
WHERE e.id IS NULL;

SELECT b.title, a.first_name, a.last_name
FROM books b
JOIN book_authors ba ON b.id = ba.book_id
JOIN authors a ON ba.author_id = a.id;

SELECT g.name, b.title
FROM genres g
LEFT JOIN books b ON g.id = b.genre_id;

SELECT m.first_name, m.last_name, b.title
FROM members m
LEFT JOIN loans l ON m.id = l.member_id
LEFT JOIN books b ON l.book_id = b.id;

SELECT m.first_name, m.last_name, b.title, l.loan_date, COALESCE(l.return_date, 'Not returned') AS return_date
FROM loans l
JOIN members m ON l.member_id = m.id
JOIN books b ON l.book_id = b.id;
