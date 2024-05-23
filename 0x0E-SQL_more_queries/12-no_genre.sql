-- Import the database dump of hbtn_0d_tvshows to your MySQL server
-- $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p 
-- $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
-- A script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows 
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
