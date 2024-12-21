import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Data Pengunjung Wisata
pengunjung_a = []  # Menyimpan data pengunjung wisata A
pengunjung_b = []  # Menyimpan data pengunjung wisata B
rata_rata_a = []   # Menyimpan rata-rata pengunjung wisata A
rata_rata_b = []   # Menyimpan rata-rata pengunjung wisata B

# Fungsi untuk menghitung rata-rata pengunjung
def hitung_rata_rata(data):
    return sum(data) / len(data) if data else 0

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(pengunjung_a) + 1), rata_rata_a, label='Wisata A', marker='o', linestyle='-')
    plt.plot(range(1, len(pengunjung_b) + 1), rata_rata_b, label='Wisata B', marker='o', linestyle='-')
    plt.title('Perbandingan Rata-rata Pengunjung: Wisata A vs Wisata B')
    plt.xlabel('Minggu ke')
    plt.ylabel('Rata-rata Pengunjung')
    plt.legend()
    plt.grid(True)
    plt.show()

# Fungsi untuk mencetak tabel data pengunjung dan rata-rata
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Minggu", "Pengunjung A", "Pengunjung B", "Rata-rata A", "Rata-rata B"]
    # Gunakan panjang data yang lebih kecil untuk menghindari IndexError
    min_len = min(len(pengunjung_a), len(pengunjung_b))
    for i in range(min_len):
        table.add_row([i+1, pengunjung_a[i], pengunjung_b[i], rata_rata_a[i], rata_rata_b[i]])
    print(table)

# Program utama
minggu = 1  # Mulai dengan minggu 1
while True:
    try:
        # Otomatis input data pengunjung berdasarkan minggu
        print(f"\nMasukkan jumlah pengunjung untuk Minggu ke-{minggu}:")
        
        # Mengisi data pengunjung untuk Wisata A dan B secara manual
        pengunjung_a_minggu = int(input(f"  Wisata A: "))
        pengunjung_b_minggu = int(input(f"  Wisata B: "))

        if pengunjung_a_minggu < 0 or pengunjung_b_minggu < 0:
            print("Masukkan jumlah pengunjung yang positif!")
            continue

        # Menyimpan data pengunjung untuk setiap minggu
        pengunjung_a.append(pengunjung_a_minggu)
        pengunjung_b.append(pengunjung_b_minggu)

        # Hitung rata-rata pengunjung setelah setiap input data
        rata_rata_a.append(hitung_rata_rata(pengunjung_a))
        rata_rata_b.append(hitung_rata_rata(pengunjung_b))

        # Cetak tabel rata-rata pengunjung
        print_execution_table()

        # Perbarui grafik
        update_graph()

        # Meningkatkan minggu
        minggu += 1

        # Tanyakan apakah lanjutkan
        lanjut = input("\nApakah Anda ingin melanjutkan ke minggu berikutnya? (y/n): ").strip().lower()
        if lanjut != 'y':
            print("Program selesai. Terima kasih!")
            break

    except ValueError:
        print("Masukkan nilai yang valid!")