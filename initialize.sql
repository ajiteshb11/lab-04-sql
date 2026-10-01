-- Create users table
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at DATETIME NOT NULL
);

-- Create posts table
CREATE TABLE IF NOT EXISTS posts (
    post_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    content TEXT,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Add users
INSERT INTO users VALUES
(1, 'ajitesh', 'ajitesh@example.com', '2026-09-01 10:00:00'),
(2, 'alex', 'alex@example.com', '2026-09-02 11:00:00'),
(3, 'maya', 'maya@example.com', '2026-09-03 12:00:00'),
(4, 'jordan', 'jordan@example.com', '2026-09-04 13:00:00'),
(5, 'sam', 'sam@example.com', '2026-09-05 14:00:00'),
(6, 'chris', 'chris@example.com', '2026-09-06 15:00:00'),
(7, 'taylor', 'taylor@example.com', '2026-09-07 16:00:00'),
(8, 'jamie', 'jamie@example.com', '2026-09-08 17:00:00'),
(9, 'morgan', 'morgan@example.com', '2026-09-09 18:00:00'),
(10, 'casey', 'casey@example.com', '2026-09-10 19:00:00');

-- Add posts
INSERT INTO posts VALUES
(1, 1, 'First Post', 'Learning SQL is fun.', '2026-09-11 10:00:00'),
(2, 2, 'Databases', 'Working with MySQL.', '2026-09-12 11:00:00'),
(3, 3, 'Python', 'Using Python with databases.', '2026-09-13 12:00:00'),
(4, 1, 'SQL Queries', 'Practicing SELECT statements.', '2026-09-14 13:00:00'),
(5, 4, 'Data Science', 'Exploring data science.', '2026-09-15 14:00:00'),
(6, 5, 'UVA', 'Another day at UVA.', '2026-09-16 15:00:00'),
(7, 6, 'Joins', 'Learning how SQL joins work.', '2026-09-17 16:00:00'),
(8, 7, 'ETL', 'Building data pipelines.', '2026-09-18 17:00:00'),
(9, 8, 'Analytics', 'Analyzing some data.', '2026-09-19 18:00:00'),
(10, 1, 'More SQL', 'Getting better at SQL.', '2026-09-20 19:00:00');
