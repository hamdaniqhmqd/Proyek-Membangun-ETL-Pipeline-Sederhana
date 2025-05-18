from utils.extract import extract_data_from_page
from utils.transform import clean_and_transform_data
from utils.load import save_to_csv, save_to_postgresql

def main():
    """Fungsi utama untuk menjalankan proses ETL: Extract, Transform, Load."""
    base_url = 'https://fashion-studio.dicoding.dev/'
    all_products = []

    # Mulai scraping dari halaman utama
    print(f"Memulai scraping dari halaman utama: {base_url}")
    try:
        products = extract_data_from_page(base_url)
        all_products.extend(products)
    except Exception as error:
        print(f"Gagal mengambil data dari halaman utama: {error}")

    # Lanjut scraping dari halaman 2 sampai 50
    for page_number in range(2, 51):
        page_url = f"{base_url}page{page_number}"
        print(f"Scraping halaman ke-{page_number}: {page_url}")
        try:
            products = extract_data_from_page(page_url)
            all_products.extend(products)
        except Exception as error:
            print(f"Gagal mengambil data dari halaman {page_number}: {error}")

    # Jika tidak ada data yang berhasil diambil
    if not all_products:
        print("Tidak ada data produk yang berhasil diambil. Program dihentikan.")
        return

    # Transformasi dan pembersihan data
    cleaned_data = clean_and_transform_data(all_products)

    # Simpan data ke file CSV
    save_to_csv(cleaned_data)

    # Simpan data ke PostgreSQL
    save_to_postgresql(cleaned_data)

    print("Proses scraping dan penyimpanan data selesai.")

# Menjalankan fungsi main
if __name__ == "__main__":
    main()
