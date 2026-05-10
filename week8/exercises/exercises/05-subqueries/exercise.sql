SELECT *
FROM students
WHERE gpa > (SELECT AVG(gpa) FROM students);

SELECT *
FROM students
WHERE id IN (
    SELECT student_id
    FROM enrollments
    WHERE course_id = (
        SELECT id FROM courses WHERE code = 'CS50'
    )
);

SELECT *
FROM students
WHERE id NOT IN (
    SELECT student_id
    FROM enrollments
    WHERE course_id = (
        SELECT id FROM courses WHERE code = 'CS50'
    )
);

SELECT *
FROM courses
WHERE teacher_id = (
    SELECT id FROM teachers WHERE salary = (SELECT MAX(salary) FROM teachers)
);

SELECT s.*
FROM students s
JOIN (
    SELECT student_id, COUNT(*) AS course_count
    FROM enrollments
    GROUP BY student_id
) ec ON s.id = ec.student_id
WHERE ec.course_count >= 3;

SELECT *
FROM members
WHERE id IN (
    SELECT member_id
    FROM loans
    GROUP BY member_id
    HAVING COUNT(*) > 2
);

SELECT *
FROM books
WHERE pages > (SELECT AVG(pages) FROM books);

SELECT *
FROM students s
WHERE EXISTS (
    SELECT 1
    FROM enrollments e
    JOIN grades g ON g.enrollment_id = e.id
    WHERE e.student_id = s.id
);

SELECT *
FROM courses c
WHERE NOT EXISTS (
    SELECT 1
    FROM enrollments e
    JOIN grades g ON g.enrollment_id = e.id
    WHERE e.course_id = c.id
);

SELECT *
FROM courses
WHERE id IN (
    SELECT course_id
    FROM enrollments
    GROUP BY course_id
    HAVING COUNT(*) = (
        SELECT MAX(count)
        FROM (
            SELECT COUNT(*) AS count
            FROM enrollments
            GROUP BY course_id
        )
    )
);
