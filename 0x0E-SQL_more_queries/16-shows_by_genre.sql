-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
     INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
     INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
