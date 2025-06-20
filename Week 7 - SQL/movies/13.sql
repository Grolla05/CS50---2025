SELECT DISTINCT(p.name)
FROM people AS p
JOIN stars AS s ON p.id = s.person_id
WHERE s.movie_id IN (
    SELECT s_inner.movie_id
    FROM stars AS s_inner
    JOIN people AS p_inner ON s_inner.person_id = p_inner.id
    WHERE p_inner.name = 'Kevin Bacon' AND p_inner.birth = 1958
) AND p.name != 'Kevin Bacon';
