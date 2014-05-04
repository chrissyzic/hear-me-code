'''For reference (this is what should print out):
Adaptation, R, 3, 7.8, Comedy / Crime / Drama
The Hours, PG-13, 3, , 7.6, Drama
Kramer vs. Kramer, PG, 3, 7.8, Drama
Manhattan, R, 1, 8.1, Comedy / Drama / Romance
Sophie's Choice, R, 3, 7.7, Drama / Romance
'''

movie_titles = ['Adaptation', 'The Hours', 'Kramer v. Kramer', 'Manhattan', '''Sophie's Choice''']
parental_ratings = ['R', 'PG-13', 'PG', 'R', 'R']
bechdel_ratings = ['3', '3', '3', '1', '3']
imdb_ratings = ['7.8', '7.6', '7.8', '8.1', '7.7']
movie_genres = ['Comedy / Crime / Drama', 'Drama', 'Drama', 'Comedy / Drama / Romance', 'Drama / Romance']

for movie, parental, bechdel, imdb, genre in zip(movie_titles, parental_ratings, bechdel_ratings, imdb_ratings, movie_genres):
    print "{0}, {1}, {2}, {3}, {4}".format(movie,parental,bechdel,imdb,genre)
