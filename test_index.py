from index import *
def test_movie_with_longest_runtime():
    assert movie_with_longest_runtime() == [('Never Sleep Again: The Elm Street Legacy', 480.0, 11415)]

def test_num_actors_in_longest_movie():
    assert num_actors_in_longest_movie() == [(6,)]

def test_shortest_movie_in_2006():
    assert shortest_movie_in_2006() == [('The Guardian',)]

def test_actors_in_toy_story():
    assert actors_in_toy_story() == [('Tom Hanks',), ('Jim Varney',),
 ('Wallace Shawn',), ('Don Rickles',), ('John Ratzenberger',), ('Tim Allen',)]

def test_director_of_toy_story():
    assert director_of_toy_story() == [('John Lasseter',)]

def test_names_of_writers_of_toy_story():
    assert names_of_writers_of_toy_story() == [('Joss Whedon',), ('Joel Cohen',), ('Andrew Stanton',), 
            ('Alec Sokolow',)]

def test_actor_id_and_name_with_most_movie_credits():
    assert actor_id_and_name_with_most_movie_credits() == [('Robert De Niro', 429, 78)]
    # actor_name, id, count of movie credits

def test_titles_of_movies_of_previous_actor_post_2005_length():
    movie_titles = titles_of_movies_of_previous_actor_post_2005() 
    assert len(movie_titles) == 28

def test_titles_of_movies_of_previous_actor_post_2005_names():
    movie_titles = titles_of_movies_of_previous_actor_post_2005() 
    assert movie_titles[:5] == [("New Year's Eve",), ('Mr. Warmth: The Don Rickles Project',),
 ('Hands of Stone',), ('Last Vegas',), ('I Knew It Was You: Rediscovering John Cazale',)]

def test_titles_of_movies_with_over_three_directors():
    movies_mult_directors = titles_of_movies_with_over_three_directors()
    assert len(movies_mult_directors) == 22

def test_most_prolific_writer_2018():
    assert most_prolific_writer_2018() == [('Ryan Engle', 3)]

def test_most_prolific_actor_2010_to_2015():
    assert most_prolific_actor_2010_to_2015() == [('James Franco', 22)]

def test_all_actors_over_three_movies_in_2010():
    assert all_actors_over_three_movies_in_2010() == [('Aaron Taylor-Johnson',),
 ('Adam Scott',), ('Barry Pepper',), ('Ben Stiller',), ('Danny Huston',), ('Gemma Arterton',),
 ('Helen Mirren',), ('Jay Baruchel',), ('Jessica Alba',), ('Jonah Hill',), ('Josh Brolin',),
 ('Josh Duhamel',), ('Keith David',), ('Liam Neeson',), ('Matt Damon',), ('Melissa Leo',),
 ('Patricia Clarkson',), ('Pierce Brosnan',), ('Ralph Fiennes',), ('Susan Sarandon',), ('Zach Galifianakis',)]

def test_spielbergs_most_used_studio():
    assert spielbergs_most_used_studio() == [('Universal Pictures', 7)]

def test_years_of_two_spielberg_movies():
    assert years_of_two_spielberg_movies() == [(1989, 2), (1993, 2), (1997, 2), (2002, 2), 
            (2005, 2), (2011, 2), (2018, 2)]

def test_num_of_movies_for_toy_story_actors():
    assert num_of_movies_for_toy_story_actors() == [('Tom Hanks', 46),
 ('Jim Varney', 8), ('Wallace Shawn', 27), ('Don Rickles', 10), ('John Ratzenberger', 7),
 ('Tim Allen', 20)]

def test_movies_of_toy_story_director():
    assert movies_of_toy_story_director() == [('Cars 2',), ('Cars',), ("A Bug's Life",), 
            ('Toy Story 2',), ('Toy Story',)]
def test_names_of_tom_hanks_directors():
    # actor id 189
    assert names_of_tom_hanks_directors() == [('Robert Zemeckis',), ('Tom Hanks',), ('Penny Marshall',), ('Chris Paine',), ('Doug Nichol',),
 ('Steven Spielberg',), ('Tom Tykwer',), ('Sam Mendes',), ('Steve Purcell (II)',), ('Nora Ephron',),
 ('Paul Greengrass',), ('Ron Howard',), ('Stephen Daldry',), ('James Ponsoldt',), ('Frank Darabont',),
 ('David Seltzer',), ('Meg Ryan',), ('Lana Wachowski',), ('Lilly Wachowski',), ('Dario Argento',),
 ('Angus MacLane',), ('Clint Eastwood',), ('Lee Unkrich',), ('John Lasseter',), ('Joel Coen',),
 ('Alexander Mackendrick',), ('Ethan Coen',), ('Tom Mankiewicz',), ('Stan Dragoti',), ('Mike Nichols',),
 ('Kevin Pollak',), ('Roger Spottiswoode',), ('Joe Dante',),
 ('John Patrick Shanley',), ('Garry Marshall',), ('John Lee Hancock',),
 ('Brian DePalma',)] 

def test_director_tom_hanks_worked_with_most():
    assert director_tom_hanks_worked_with_most() == [('Steven Spielberg', 5)]

def test_names_of_all_tom_hanks_writers():
    th_directors = names_of_all_tom_hanks_writers() 
    len(th_directors) == 78
    assert th_directors[:5] == [('Eric Roth',),
 ('Nia Vardalos',), ('Tom Hanks',), ('Gary Ross',), ('Anne Spielberg',)]
    


    
