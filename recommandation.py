import pandas as pd

# Load Movies Metadata
metadata = pd.read_csv("movies_metadata.csv", low_memory=False)

# Print the first three rows
print(metadata.head(8))

C = metadata['vote_average'].mean()
#print(C)

m = metadata['vote_count'].quantile(0.95)
#print(m)

# Filter out all qualified movies into a new DataFrame
q_movies = metadata.copy().loc[metadata['vote_count'] >= m]
q_movies.shape

# Function that computes the weighted rating of each movie
def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

#Sort movies based on score calculated above
q_movies = q_movies.sort_values('score', ascending=False)


#Print the top 15 movies
print(q_movies[['title', 'vote_count', 'vote_average', 'score']].head(3))

ratings_mean_count = metadata.groupby('title')['vote_average'].mean().sort_values(ascending=False).head(3)
print(ratings_mean_count)

ratings_mean_count = metadata.groupby('title')['vote_average'].count().sort_values(ascending=False).head(3)
print(ratings_mean_count)

ratings_mean_count['rating_counts'] = pd.DataFrame(metadata.groupby('title')['vote_average'].count())



