-- Analysis: User Engament (Number of Ratings per User)
SELECT 
    user_id,
    COUNT(*) AS number_of_ratings,
    AVG(rating) AS average_rating_given
FROM {{ ref('fct_ratings') }}
GROUP BY user_id
ORDER BY number_of_ratings DESC;
