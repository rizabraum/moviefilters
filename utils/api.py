import requests
import pandas as pd
from config import API_KEY, BASE_URL

def get_movies(genre, rating_min, year_min, year_max):
    url = "https://api.themoviedb.org/3/discover/movie"
    
    # Menyusun parameter untuk permintaan API
    params = {
        'api_key': API_KEY,  # Gunakan API_KEY dari config
        'with_genres': ','.join(map(str, genre)),  # Menggunakan daftar genre
        'vote_average.gte': rating_min,  # Minimum rating
        'primary_release_date.gte': f'{year_min}-01-01',  # Rentang tahun
        'primary_release_date.lte': f'{year_max}-12-31',
        'sort_by': 'popularity.desc',  # Mengurutkan berdasarkan popularitas
    }
    
    # Mengirim permintaan ke API TMDb
    response = requests.get(url, params=params)
    
    # Memeriksa apakah permintaan berhasil
    if response.status_code == 200:
        data = response.json()
        movies = data.get('results', [])
        
        # Jika tidak ada film yang ditemukan
        if not movies:
            print("Tidak ada film yang ditemukan dengan filter yang diberikan.")
            return pd.DataFrame()  # Mengembalikan DataFrame kosong jika tidak ada hasil
        
        # Menyusun data film menjadi DataFrame
        movie_list = []
        for movie in movies:
            movie_list.append({
                'Film': movie['title'],
                'Genre': movie['genre_ids'],  # ID genre, bisa diubah jika perlu untuk nama genre
                'Rating': movie['vote_average'],
                'Tahun Rilis': movie['release_date'][:4],  # Mengambil tahun rilis
            })
        
        return pd.DataFrame(movie_list)  # Mengembalikan DataFrame
    else:
        print(f"Error: Permintaan API gagal dengan status code {response.status_code}")
        return pd.DataFrame()  # Mengembalikan DataFrame kosong jika terjadi error
