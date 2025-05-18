# Submission Dicoding Fundamental Pemrosesan Data

Proyek ini merupakan submission dari kelas **Fundamental Pemrosesan Data** di Dicoding. Proyek ini melakukan proses ETL (Extract, Transform, Load) pada data produk fashion yang diambil dari situs [Fashion Studio Dicoding](https://fashion-studio.dicoding.dev/). Data diambil dari halaman 1 hingga 50, lalu dibersihkan dan disimpan ke berbagai media penyimpanan.

## Struktur Proyek

```
.
├── main.py
├── utils/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── products.csv
└── README.md
```

## Fitur

- **Extract**: Mengambil data produk dari situs menggunakan `requests` dan `BeautifulSoup`.
- **Transform**: Membersihkan dan memformat data menggunakan `pandas`.
- **Load**: Menyimpan data hasil ekstraksi dan transformasi ke:

  - File CSV (`products.csv`)
  - Database PostgreSQL

## Cara Menjalankan

### Menjalankan Proses ETL

```bash
python main.py
```

### Menjalankan Unit Test

```bash
python -m unittest discover tests
```

### Menjalankan Test Coverage

```bash
coverage run -m unittest discover tests
coverage report -m
```

## Konfigurasi Database PostgreSQL

Sesuaikan konfigurasi koneksi PostgreSQL pada fungsi `save_to_postgresql()` di `utils/load.py` sesuai lingkungan lokal Anda:

```python
username = 'postgres'
password = 'ahmad_jupiter'
host = 'localhost'
port = '5432'
database = 'product_db'
```
