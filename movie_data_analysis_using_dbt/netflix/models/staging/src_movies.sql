WITH raw_movies AS (
    SELECT * FROM MOVIELENS.RAW.RAW_MOVIES
)
SELECT 
    movieId AS movie_Id,
    title,
    genres
FROM raw_movies