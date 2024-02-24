-- mport the database dump from hbtn_0d_tvshows to your MySQL server: 
SELECT t.`title`, f.`genre_id` FROM `tv_shows` AS t INNER JOIN `tv_show_genres` AS f ON t.`id` = f.`show_id`
ORDER BY t.`title`, f.`genre_id`;
