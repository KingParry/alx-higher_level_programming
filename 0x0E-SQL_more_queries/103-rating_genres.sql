-- Import the database dump from hbtn_0d_tvshows_rate to your MySQL server:
SELECT `name`, SUM(`rate`) AS `rating` FROM `tv_genres` AS w INNER JOIN `tv_show_genres` AS l
ON l.`genre_id` = w.`id` INNER JOIN `tv_show_ratings` AS p ON p.`show_id` = l.`show_id`
GROUP BY `name`
ORDER BY `rating` DESC;
