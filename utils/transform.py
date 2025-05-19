import pandas as pd
import numpy as np
from datetime import datetime

def clean_and_transform_data(product_data: list) -> pd.DataFrame:
    """Membersihkan dan mengubah data mentah produk ke format DataFrame yang bersih."""

    if not product_data:
        return pd.DataFrame(columns=['title', 'price', 'rating', 'colors', 'size', 'gender', 'timestamp'])

    df = pd.DataFrame(product_data)

    # Filter data dengan judul "unknown"
    if 'title' in df.columns:
        df = df[~df['title'].str.lower().str.contains('unknown', na=False)]

    # Bersihkan dan ubah kolom harga menjadi float dalam satuan IDR
    df['price'] = df['price'].replace(r'[^\d.]', '', regex=True).replace('', np.nan)
    df.dropna(subset=['price'], inplace=True)
    df['price'] = df['price'].astype(float) * 16000

    # Bersihkan dan ubah kolom rating menjadi float
    df['rating'] = df['rating'].astype(str).str.extract(r'(\d+\.\d+|\d+)').replace('', np.nan)
    df.dropna(subset=['rating'], inplace=True)
    df['rating'] = df['rating'].astype(float)

    # Bersihkan dan ubah kolom colors menjadi int
    df['colors'] = df['colors'].replace(r'\D', '', regex=True).replace('', np.nan)
    df.dropna(subset=['colors'], inplace=True)
    df['colors'] = df['colors'].astype(int)

    # Hilangkan label dari kolom size dan gender
    df['size'] = df['size'].replace(r'Size:\s*', '', regex=True)
    df['gender'] = df['gender'].replace(r'Gender:\s*', '', regex=True)

    # Hapus duplikat dan nilai kosong
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Tambahkan kolom timestamp saat data diproses
    df['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return df
