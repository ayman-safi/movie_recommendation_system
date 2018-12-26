
import pandas as pd

import seaborn as sns
sns.set_style('dark')


ratings_data = pd.read_csv("ratings.csv")

ratings_data.head()

movie_names = pd.read_csv("movies.csv")

movie_names.head()

movie_data = pd.merge(ratings_data, movie_names, on='movieId')

print(movie_data)

# movie_data.groupby('title')['rating'].mean().head()

print(movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head())

ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())

ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())

user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')

forrest_gump_ratings = user_movie_rating['Forrest Gump (1994)']

print(forrest_gump_ratings.head())

movies_like_forest_gump = user_movie_rating.corrwith(forrest_gump_ratings)

corr_forrest_gump = pd.DataFrame(movies_like_forest_gump, columns=['Correlation'])

corr_forrest_gump.dropna(inplace=True)

print(corr_forrest_gump.head(5))

print(corr_forrest_gump.sort_values('Correlation', ascending=False).head(10))

corr_forrest_gump = corr_forrest_gump.join(ratings_mean_count['rating_counts'])

print(corr_forrest_gump.head())

print(corr_forrest_gump[corr_forrest_gump ['rating_counts'] > 50].sort_values('Correlation', ascending=False).head() )
