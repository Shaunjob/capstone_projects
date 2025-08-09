WITH raw_genome_scores AS (
    SELECT * FROM MOVIELENS.RAW.RAW_GENOME_SCORES
)
SELECT 
    movieId as movie_id,
    tagId AS tag_id,
    relevance
FROM raw_genome_scores