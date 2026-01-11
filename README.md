# Animepedia-Bot v2.0

Bot sederhana untuk mencari informasi seputar anime. Ini adalah pengembangan dari versi sebelumnya (v1), sekarang sudah menggunakan antarmuka web (web-based UI) dan memiliki fitur pencatatan riwayat obrolan (log history).

Dibuat menggunakan Python (Flask) dengan database simpel berbasis JSON.

## Fitur
- **Web UI:** Tampilan chat lebih interaktif dengan tema dark/stardust.
- **Respon Cepat:** Mengambil data langsung dari `data.json`.
- **Log History:** Percakapan otomatis tersimpan di file `chat_log.txt`.

## Persiapan
Pastikan di komputer sudah terinstall:
- Python (versi 3 ke atas)
- Git (opsional, bisa juga download zip)

## Cara Install (Installation)

1. **Clone Repository**
   Buka terminal/CMD, lalu download project ini:
   ```bash
   git clone https://github.com/mynameismunique/Animepedia-Bot-v2.0.git

2. **Masuk ke Folder**
   ```bash
   cd Animepedia-Bot-v2.0
3. **Install Library**
   Install framework Flask yang dibutuhkan:
   ```bash
   pip install flask

5. **Install Library**
   Start servernya dengan perintah:
   ```bash
   pyhton app.py
  (Kalau error, coba ketik python3 app.py)

  ## Cara Penggunaan (Usage)
1. **Buka Browser** Setelah server jalan (muncul tulisan `Running on http://...`), buka browser (Chrome/Firefox/Edge) dan akses: `http://127.0.0.1:5000`
2. **Mulai Chatting**
   - Ketik nama anime atau kata kunci di kolom chat, lalu tekan **Enter** atau klik **Kirim**.
   - Bot akan membalas sesuai data yang ada di `data.json`.
   - Contoh input: "Naruto","One Piece". atau sapaan biasa.
3. **Cek History Chat** Semua obrolan yang terjadi di web akan tersimpan otomatis. Kamu bisa melihat riwayatnya dengan membuka file `chat_log,txt` di dalam folder project.

  ## Struktur File
- `app.py` -> File utama backend/logika bot.
- `data.json` -> Database info anime.
- `chat_log.txt` -> File untuk menyimpan riwayat chat.
- `templates/` -> Folder berisi file HTML tampilan web.
