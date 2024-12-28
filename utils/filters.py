def filter_movies(movies_df, preferred_genre, min_rating, min_year, max_year):
    # Pastikan preferred_genre menjadi list meskipun hanya satu genre
    if isinstance(preferred_genre, int):
        preferred_genre = [preferred_genre]
    
    # Menggunakan filter untuk genre dan rentang tahun
    return movies_df[
        movies_df['Genre'].apply(lambda x: any(genre in x for genre in preferred_genre)) &  # Filter berdasarkan genre
        (movies_df['Rating'] >= min_rating) &  # Rating minimal
        (movies_df['Tahun Rilis'] >= str(min_year)) &  # Tahun mulai lebih besar atau sama dengan tahun minimum
        (movies_df['Tahun Rilis'] <= str(max_year))  # Tahun rilis lebih kecil atau sama dengan tahun maksimum
    ]
    
    return filtered_movies
