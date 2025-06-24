SELECT m.title
FROM movies AS m
JOIN stars AS s ON m.id = s.movie_id
JOIN people AS p ON s.person_id = p.id
WHERE p.name IN ('Johnny Depp', 'Helena Bonham Carter')
GROUP BY m.title
HAVING COUNT(DISTINCT p.name) = 2;
