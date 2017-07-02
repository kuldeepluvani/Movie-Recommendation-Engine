import pandas as pd
import numpy as np
import os
import webbrowser


movies = pd.read_csv('movies.csv', index_col = 'movieId')
ratings = pd.read_csv('ratings.csv')

htmlrating = ratings[1:100].to_html()
htmlmovies = movies[1:100].to_html()

#print htmlmovies
with open("ratings.html", "w") as f:
    f.write(htmlrating)

with open("movies.html", "w") as fl:
    fl.write(htmlmovies)

def openhtml(htmlfile):
    openfile = os.path.abspath(htmlfile)
    webbrowser.open("file://{}".format(openfile))

f = "ratings.html"
m = "movies.html"
openhtml(f)


'''# print movies.head()
# print ratings.head()

print("Reading files - Successfully")

def replace_name(x):
    return movies[movies['movieId'] == x].title.values[0]


ratings.movieId = ratings.movieId.map(replace_name)
M = ratings.pivot_table(index=['userId'], columns=['movieId'], values='rating')

#print ("Table has been created")

def pearson(s1, s2):
    s1_c = s1 - s1.mean()
    s2_c = s2 - s2.mean()
    return np.sum(s1_c * s2_c) / np.sqrt(np.sum(s1_c ** 2) * np.sum(s2_c ** 2))


def get_recs(movie_name, M, num):
    import numpy as np
    reviews = []
    for title in M.columns:
        if title == movie_name:
            continue
        cor = pearson(M[movie_name], M[title])
        if np.isnan(cor):
            continue
        else:
            reviews.append((title, cor))
    reviews.sort(key=lambda tup: tup[1], reverse=True)
    return reviews[:num]

#print ("Searching Movie")
#rec = get_recs('Toy Story (1995)', M, 10)

print rec[:9]
# print "HEY"
'''
