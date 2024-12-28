from sklearn.neighbors import NearestNeighbors
import pandas as pd

def recommend_movies(filtered_movies):
    # Mengonversi genre menjadi angka
    filtered_movies.loc[:, 'Genre_encoded'] = filtered_movies['Genre'].apply(lambda x: x[0] if x else 0)
    
    # Menyusun fitur untuk model KNN
    X = filtered_movies[['Genre_encoded', 'Rating', 'Tahun Rilis']].values

    # Menerapkan KNN untuk menemukan film yang mirip
    knn = NearestNeighbors(n_neighbors=3, metric='euclidean')
    knn.fit(X)

    # Menggunakan KNN untuk rekomendasi berdasarkan film pertama yang difilter
    query_movie = filtered_movies.iloc[0][['Genre_encoded', 'Rating', 'Tahun Rilis']].values.reshape(1, -1)
    recommendations = knn.kneighbors(query_movie)

    recommended_movies = filtered_movies.iloc[recommendations[1][0]]
    return recommended_movies
