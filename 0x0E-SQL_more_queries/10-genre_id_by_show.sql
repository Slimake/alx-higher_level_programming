-- url = https://s3.amazonaws.com/intranet-projects-files/holbertonschool-hi-- gher-level_programming+/274/hbtn_0d_tvshows.sql
-- Import the database dump from url into your MySQL server.

SELECT title, genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
