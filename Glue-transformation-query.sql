SELECT 
    movieId,
    title,
    genre,
    CASE 
        WHEN genre = 'Adventure' THEN 'Adventure'
        WHEN genre = 'Comedy' THEN 'Comedy'
        WHEN genre = 'Action' THEN 'Action'
        WHEN genre = 'Drama' THEN 'Drama'
        WHEN genre = 'Horror' THEN 'Horror'
        WHEN genre = 'Crime' THEN 'Crime'
        WHEN genre = 'Children' THEN 'Children'
        ELSE 'Other'
    END AS genre_classification
FROM myDataSource
