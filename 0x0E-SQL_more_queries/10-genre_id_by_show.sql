

CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;
USE hbtn_0d_tvshows;
SOURCE hbtn_0d_tvshows;
SELECT title, genre_id 
FROM tv_shows, tv_show_genres 
WHERE tv_show_genres.show_id = tv_shows.id 
ORDER BY tv_shows.title, tv_show_genres.genre_id;
