--  script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- Lists shows
  SELECT shows.title, genres.genre_id
    FROM tv_shows AS shows
         LEFT JOIN tv_show_genres AS genres
         ON shows.id = genres.show_id
         WHERE genres.show_id IS NULL
ORDER BY shows.title ASC, genres.genre_id ASC;
