-- Join users and posts and return posts created by user 1
SELECT
    users.username,
    posts.title,
    posts.content,
    posts.created_at
FROM users
JOIN posts
    ON users.user_id = posts.user_id
WHERE users.user_id = 1;