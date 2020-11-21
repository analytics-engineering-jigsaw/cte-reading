import sqlite3
conn = sqlite3.connect('films.db')
cursor = conn.cursor()

def movie_with_longest_runtime():
    cursor.execute("""SELECT title, runtime, id
  FROM movies
 ORDER BY runtime DESC LIMIT 1;
""")

    return cursor.fetchall()

def num_actors_in_longest_movie():
    cursor.execute("""SELECT COUNT( * ) FROM movie_actors
 WHERE movie_id = 480;""")
    return cursor.fetchall()

def shortest_movie_in_2006():
    cursor.execute(""" SELECT title FROM movies
 WHERE year = 2006 ORDER BY runtime LIMIT 1;
""")
    return cursor.fetchall()

def actors_in_toy_story():
    # movie id 3648
    cursor.execute("""
SELECT a.name
  FROM movie_actors AS ma
       JOIN
       actors AS a ON ma.actor_id = a.id
 WHERE ma.movie_id = 3648;
 """)
    return cursor.fetchall()

def director_of_toy_story():
    cursor.execute("""
SELECT d.name
  FROM movie_directors AS md JOIN
       directors AS d ON md.director_id = d.id
 WHERE md.movie_id = 3648;
""")
    return cursor.fetchall()

def names_of_writers_of_toy_story():
    cursor.execute("""
SELECT w.name FROM movie_writers AS mw
       JOIN writers AS w ON mw.writer_id = w.id
 WHERE mw.movie_id = 3648;""")
    return cursor.fetchall()

def actor_id_and_name_with_most_movie_credits():
    # actor_name, id, and number_of_movie credits
    cursor.execute(""" SELECT a.name,
       a.id, COUNT( * )
  FROM movie_actors AS ma JOIN
       actors a ON ma.actor_id = a.id
 GROUP BY ma.actor_id ORDER BY COUNT( * ) DESC LIMIT 1;
""")
    return cursor.fetchall()

def titles_of_movies_of_previous_actor_post_2005():
    cursor.execute("""
SELECT m.title
  FROM movie_actors AS ma
       JOIN
       movies AS m ON ma.movie_id = m.id
 WHERE ma.actor_id = 429 AND
       m.year > 2005;
""")
    return cursor.fetchall()

def titles_of_movies_with_over_three_directors():
    cursor.execute("""
SELECT m.title
  FROM movie_directors AS md
       JOIN
       movies AS m ON md.movie_id = m.id
 GROUP BY m.id
HAVING COUNT( * ) > 3;
""")
    movies_mult_directors = cursor.fetchall()
    return movies_mult_directors 

def most_prolific_writer_2018():
    cursor.execute("""
SELECT w.name,
       count( * )
  FROM movie_writers AS mw
       JOIN
       writers AS w ON mw.writer_id = w.id
       JOIN
       movies AS m ON mw.movie_id = m.id
 WHERE m.year = 2018
 GROUP BY w.id
 ORDER BY count( * ) DESC LIMIT 1;
""")
    return cursor.fetchall()

def most_prolific_actor_2010_to_2015():
    cursor.execute("""
SELECT a.name,
       count( * )
  FROM movie_actors AS ma
       JOIN
       actors AS a ON ma.actor_id = a.id
       JOIN
       movies AS m ON ma.movie_id = m.id
 WHERE m.year >= 2010 AND m.year <= 2015
 GROUP BY a.id
 ORDER BY count( * ) DESC LIMIT 1;
""")
    return cursor.fetchall()

def all_actors_over_three_movies_in_2010():
    cursor.execute("""
SELECT a.name
  FROM movie_actors AS ma
       JOIN
       movies AS m ON ma.movie_id = m.id
       JOIN
       actors AS a ON ma.actor_id = a.id
   WHERE m.year = 2010
   GROUP BY a.name
   HAVING COUNT(*) > 3;
""")
    return cursor.fetchall()

def spielbergs_most_used_studio():
    cursor.execute("""
SELECT m.studio,
       COUNT( * )
  FROM movie_directors AS md
       JOIN
       movies AS m ON md.movie_id = m.id
       JOIN
       directors AS d ON md.director_id = d.id
 WHERE d.name = "Steven Spielberg"
 GROUP BY m.studio
 ORDER BY COUNT( * ) DESC
 LIMIT 1;
""")
    return cursor.fetchall()

def years_of_two_spielberg_movies():
    cursor.execute("""
SELECT m.year,
       COUNT( * )
  FROM movie_directors AS md
       JOIN
       movies AS m ON md.movie_id = m.id
       JOIN
       directors AS d ON md.director_id = d.id
 WHERE d.name = "Steven Spielberg"
 GROUP BY m.year
 HAVING COUNT(*) = 2;
""")
    return cursor.fetchall()

def num_of_movies_for_toy_story_actors():
    cursor.execute("""
SELECT c.name,
       COUNT( * )
  FROM (
           SELECT actor_id
             FROM movie_actors
            WHERE movie_id = 3648
       )
       AS a
       JOIN
       movie_actors AS b ON a.actor_id = b.actor_id
       JOIN
       actors c ON a.actor_id = c.id
 GROUP BY a.actor_id;
""")
    return cursor.fetchall()

def movies_of_toy_story_director():
    cursor.execute("""
SELECT title
  FROM (
           SELECT director_id
             FROM movie_directors
            WHERE movie_id = 3648
       )
       AS a
       JOIN
       movie_directors AS b ON a.director_id = b.director_id
       JOIN
       movies c ON b.movie_id = c.id;
""")
    return cursor.fetchall()

def names_of_tom_hanks_directors():
    # actor id 189
    cursor.execute("""
SELECT DISTINCT c.name 
  FROM (
           SELECT movie_id
             FROM movie_actors
            WHERE actor_id = 189
       )
       AS a
       JOIN
       movie_directors AS b ON a.movie_id = b.movie_id
       JOIN
       directors c ON b.director_id = c.id;
""")
    return cursor.fetchall()

def director_tom_hanks_worked_with_most():
    cursor.execute("""
SELECT c.name, COUNT(*)
  FROM (
           SELECT movie_id
             FROM movie_actors
            WHERE actor_id = 189
       )
       AS a
       JOIN
       movie_directors AS b ON a.movie_id = b.movie_id
       JOIN
       directors c ON b.director_id = c.id
    GROUP BY c.name
    ORDER BY COUNT(*) DESC LIMIT 1;
""")
    return cursor.fetchall()

def names_of_all_tom_hanks_writers():
    cursor.execute("""
SELECT DISTINCT c.name
  FROM (
           SELECT movie_id
             FROM movie_actors
            WHERE actor_id = 189
       )
       AS a
       JOIN
       movie_writers AS b ON a.movie_id = b.movie_id
       JOIN
       writers c ON b.writer_id = c.id;
""")
    tom_hanks_directors = cursor.fetchall()
    return tom_hanks_directors

    
    
    

