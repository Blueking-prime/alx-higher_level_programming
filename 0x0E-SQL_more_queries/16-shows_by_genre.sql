--  script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- Lists shows
  SELECT shows.title, genres.name
    FROM tv_shows AS shows
         LEFT JOIN tv_show_genres AS link
         ON shows.id = link.show_id

         LEFT JOIN tv_genres AS genres
         ON genres.id = link.genre_id
ORDER BY shows.title ASC, genres.name ASC;
