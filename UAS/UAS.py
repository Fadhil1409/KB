import itertools

def jadwalkan_lampu_lalu_lintas(jalur):
    # Menentukan durasi maksimal berdasarkan volume kendaraan
    durasi_max = max(jalur.values())
    durasi = list(range(1, durasi_max + 1))  # Durasi yang mungkin dari 1 hingga durasi_max

    # Membuat semua kombinasi durasi untuk setiap jalur
    kombinasi_terbaik = None
    total_waktu_min = float('inf')

    for kombinasi in itertools.product(durasi, repeat=len(jalur)):
        total_waktu = sum(kombinasi)
        if total_waktu < total_waktu_min:
            total_waktu_min = total_waktu
            kombinasi_terbaik = kombinasi

    return list(zip(jalur.keys(), kombinasi_terbaik)), total_waktu_min


# Contoh data volume kendaraan di setiap jalur
jalur = {
    'A': 30,
    'B': 50,
    'C': 20,
    'D': 40
}

# Menjadwalkan lampu lalu lintas
jadwal, total_waktu = jadwalkan_lampu_lalu_lintas(jalur)

# Menampilkan jadwal lampu hijau untuk setiap jalur
for green_time in jadwal:
    print(f"{green_time[1]} detik")

# Menampilkan total waktu yang dibutuhkan
print(f"\n{total_waktu} detik")
