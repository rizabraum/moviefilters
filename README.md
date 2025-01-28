# Aplikasi Rekomendasi Film

## Deskripsi Proyek
Aplikasi ini merupakan aplikasi GUI (Graphical User Interface) berbasis Python yang memungkinkan pengguna untuk mencari rekomendasi film berdasarkan genre, rating, dan tahun rilis. Data film diambil dari API The Movie Database (TMDb).

## Fitur Utama
1. **Pencarian Berdasarkan Genre**: Pilih hingga beberapa genre untuk memfilter hasil.
2. **Pencarian Berdasarkan Rating**: Tentukan rating minimal (0-10).
3. **Pencarian Berdasarkan Tahun Rilis**: Tentukan rentang tahun rilis untuk hasil yang lebih relevan.
4. **Hasil yang Ditampilkan**: Menampilkan judul film, tahun rilis, rating, dan genre dalam format rapi dan terurut.
5. **Antarmuka GUI**: Mudah digunakan dengan fitur reset untuk memulai pencarian baru.

## Prasyarat
- Python 3.x
- API Key dari [TMDb](https://www.themoviedb.org/).

## Instalasi
1. Clone repositori ini atau salin kode ke dalam folder lokal.
2. Pastikan Anda memiliki Python 3.x terinstal di sistem Anda.
3. Instal semua pustaka yang diperlukan:

   ```bash
   pip install -r requirements.txt
   ```

4. Tambahkan file `config.py` dengan konten berikut:

   ```python
   API_KEY = "<API_KEY_ANDA>"
   ```
   Ganti `<API_KEY_ANDA>` dengan API Key Anda dari TMDb.

## Cara Menjalankan
1. Jalankan aplikasi dengan perintah berikut:

   ```bash
   python app.py
   ```

2. Antarmuka GUI akan muncul, di mana Anda dapat memilih genre, rating, dan rentang tahun rilis.
3. Klik tombol "Cari Film" untuk mendapatkan hasil rekomendasi.
4. Klik tombol "Reset Pencarian" untuk membersihkan pilihan dan memulai pencarian baru.

## File Pendukung
- `requirements.txt`: Berisi daftar pustaka yang dibutuhkan.
- `config.py`: Berisi API Key TMDb (harus dibuat oleh pengguna).

## Pustaka yang Digunakan
1. `tkinter`: Untuk antarmuka GUI.
2. `requests`: Untuk mengakses API TMDb.
3. `pandas`: Untuk manipulasi dan pengolahan data.

## Struktur Tampilan
1. **Genre**: Checkbox untuk memilih genre (dibagi dalam 4 kolom untuk keteraturan).
2. **Input**:
   - Rating Minimal
   - Tahun Rilis Minimal
   - Tahun Rilis Maksimal
3. **Hasil Pencarian**: Ditampilkan di kotak teks yang diperlebar untuk kenyamanan membaca, dilengkapi dengan penomoran dan pemisahan antar hasil.

## Contoh Hasil
1. The Shawshank Redemption (1994) | Rating: 9.3 | Genre: Drama, Kejahatan

2. Interstellar (2014) | Rating: 8.6 | Genre: Fiksi Ilmiah, Petualangan

## Lisensi
Project ini dibuat untuk tujuan pembelajaran dan penggunaan pribadi saya.
