import tkinter as tk
from tkinter import messagebox
import requests
import pandas as pd
from config import API_KEY

# Global list to manage selected genres
selected_genres = []

def get_movies(genre, rating_min, year_min, year_max):
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        'api_key': API_KEY,
        'with_genres': ','.join(map(str, genre)),
        'vote_average.gte': rating_min,
        'primary_release_date.gte': f'{year_min}-01-01',
        'primary_release_date.lte': f'{year_max}-12-31',
        'sort_by': 'popularity.desc'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        movies = data.get('results', [])

        if not movies:
            messagebox.showinfo("Tidak Ada Film", "Tidak ada film yang ditemukan dengan filter yang diberikan.")
            return pd.DataFrame()

        movie_list = []
        for movie in movies:
            movie_list.append({
                'Film': movie['title'],
                'Genre': movie['genre_ids'],
                'Rating': movie['vote_average'],
                'Tahun Rilis': movie['release_date'][:4],
            })
        return pd.DataFrame(movie_list)
    else:
        messagebox.showerror("Error", f"API request failed with status code {response.status_code}")
        return pd.DataFrame()

def get_genre_names(genre_ids):
    genre_map = {
        28: "Aksi", 12: "Petualangan", 18: "Drama", 35: "Komedi", 80: "Kejahatan",
        53: "Thriller", 10749: "Romantis", 878: "Fiksi Ilmiah", 16: "Animasi", 10402: "Musik",
        14: "Fantasi", 27: "Horor", 10751: "Keluarga", 36: "Sejarah", 10752: "Perang", 37: "Western"
    }
    return [genre_map.get(genre_id, "Unknown") for genre_id in genre_ids]

def update_selected_genres(var, genre_value):
    """Update selected_genres list based on Checkbutton changes."""
    if var.get() == 1:
        selected_genres.append(genre_value)
    else:
        selected_genres.remove(genre_value)

def show_recommendations():
    try:
        rating_min = float(rating_var.get())
        year_min = int(year_min_var.get())
        year_max = int(year_max_var.get())

        if rating_min < 0 or rating_min > 10:
            raise ValueError("Rating minimal harus antara 0 dan 10")
        if year_min > year_max:
            raise ValueError("Tahun mulai tidak boleh lebih besar dari tahun akhir")

        movies_df = get_movies(genre=selected_genres, rating_min=rating_min, year_min=year_min, year_max=year_max)

        if movies_df.empty:
            return

        movies_df['Genre Lengkap'] = movies_df['Genre'].apply(lambda x: get_genre_names(x))
        movies_df = movies_df.sort_values(by='Tahun Rilis', ascending=True)

        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)

        for idx, row in enumerate(movies_df.iterrows(), start=1):
            _, row_data = row
            output_text.insert(tk.END, f"{idx}. {row_data['Film']} ({row_data['Tahun Rilis']}) | Rating: {row_data['Rating']:.2f} | Genre: {', '.join(row_data['Genre Lengkap'])}\n\n")

        output_text.config(state=tk.DISABLED)

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))

def reset_search():
    global selected_genres
    selected_genres = []
    for var in checkbutton_vars:
        var.set(0)
    rating_var.set('')
    year_min_var.set('')
    year_max_var.set('')
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("Screen Movies")

rating_var = tk.StringVar()
year_min_var = tk.StringVar()
year_max_var = tk.StringVar()

tk.Label(root, text="Pilih Genre Film:", anchor="w").grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Genre Checkbuttons
genre_frame = tk.Frame(root)
genre_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

genres = [
    ("Aksi", 28), ("Petualangan", 12), ("Drama", 18), ("Komedi", 35), ("Kejahatan", 80),
    ("Thriller", 53), ("Romantis", 10749), ("Fiksi Ilmiah", 878), ("Animasi", 16), ("Musik", 10402),
    ("Fantasi", 14), ("Horor", 27), ("Keluarga", 10751), ("Sejarah", 36), ("Perang", 10752), ("Western", 37)
]

checkbutton_vars = []
for idx, (genre_name, genre_value) in enumerate(genres):
    var = tk.IntVar()
    checkbutton_vars.append(var)
    tk.Checkbutton(
        genre_frame, text=genre_name, variable=var,
        command=lambda v=var, gv=genre_value: update_selected_genres(v, gv)
    ).grid(row=idx // 4, column=idx % 4, sticky="w", padx=5, pady=5)

# Input Fields
tk.Label(root, text="Rating Minimal (0-10):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=rating_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Tahun Rilis Minimal:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=year_min_var).grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Tahun Rilis Maksimal:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=year_max_var).grid(row=4, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Cari Film", command=show_recommendations).grid(row=5, column=0, pady=10)
tk.Button(root, text="Reset Pencarian", command=reset_search).grid(row=5, column=1, pady=10)

# Output Area
output_text = tk.Text(root, wrap="word", height=20, width=70, state=tk.DISABLED)
output_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
