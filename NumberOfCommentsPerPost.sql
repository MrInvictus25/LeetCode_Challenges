-- Table: Submissions

-- +---------------+----------+
-- | Column Name   | Type     |
-- +---------------+----------+
-- | sub_id        | int      |
-- | parent_id     | int      |
-- +---------------+----------+
-- This table may have duplicate rows.
-- Each row can be a post or comment on the post.
-- parent_id is null for posts.
-- parent_id for comments is sub_id for another post in the table.

-- Write a solution to find the number of comments per post.
-- The result table should contain post_id and its corresponding number_of_comments.

-- The Submissions table may contain duplicate comments. You should count the number of unique comments per post.
-- The Submissions table may contain duplicate posts. You should treat them as one post.

-- The result table should be ordered by post_id in ascending order.
-- The result format is in the following example.

select post.sub_id as post_id, count(distinct number.sub_id) as number_of_comments
from Submissions post
left join Submissions number on (post.sub_id = number.parent_id)
where post.parent_id is NULL
group by post.sub_id
