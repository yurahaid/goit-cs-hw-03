SELECT *
FROM tasks
WHERE user_id = 61;

SELECT *
FROM tasks
WHERE status_id = (SELECT id FROM status WHERE name = 'new');

UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = 2;

SELECT *
FROM users
WHERE id NOT IN (SELECT user_id FROM tasks WHERE user_id = users.id);

INSERT INTO tasks (user_id, status_id, title, description)
VALUES (61, (SELECT id FROM status WHERE name = 'new'), 'New Task title', 'New Task Description');

SELECT *
FROM tasks
WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

DELETE
FROM tasks
WHERE id = 3;

SELECT *
FROM users
WHERE email LIKE '%example@domain.com%';

UPDATE users
SET fullname = 'new name'
WHERE id = 61;

SELECT COUNT(id), (select name FROM status WHERE id = tasks.status_id)
FROM tasks
GROUP BY status_id;


SELECT tasks.*
FROM tasks
         JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com';

SELECT *
FROM tasks
WHERE description IS NULL;


SELECT *
FROM users
         INNER JOIN tasks ON users.id = tasks.user_id
         INNER JOIN status ON tasks.status_id = status.id
WHERE status.name = 'in progress';


SELECT users.*, COUNT(tasks.id) AS task_count
FROM users
         LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.id;