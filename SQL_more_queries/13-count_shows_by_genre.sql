-- Number of show by genre
SELECT tv_genres.name AS 'genre', COUNT(tv_shows.id) AS 'number_of_shows' FROM tv_show_genres LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_shows.id IS NOT NULL GROUP BY tv_genres.name ORDER BY COUNT(tv_shows.id) DESC;
