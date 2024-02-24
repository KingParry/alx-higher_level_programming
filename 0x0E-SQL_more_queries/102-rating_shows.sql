-- Import the database hbtn_0d_tvshows_rate dump to your MySQL server: 
SELECT `title`, SUM(`rate`) AS `rating` FROM `tv_shows` AS f INNER JOIN `tv_show_ratings` AS g ON f.`id` = g.`show_id`
GROUP BY `title`
 ORDER BY `rating` DESC;
