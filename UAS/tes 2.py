
def jadwalkan_lampu_greedy(jalur):
    total_volume = sum(jalur.values())
    
    jadwal = {}
    total_waktu = 0
    
    for nama_jalur, volume in jalur.items():

        durasi_hijau = round(volume / total_volume * 100)
        jadwal[nama_jalur] = durasi_hijau
        total_waktu += durasi_hijau

    return jadwal, total_waktu

jalur = {
    'A': 30,
    'B': 50,
    'C': 20,
    'D': 40
}

jadwal, total_waktu = jadwalkan_lampu_greedy(jalur)

print("Jadwal Lampu Hijau:")
for jalur, durasi in jadwal.items():
    print(f"Jalur {jalur}: {durasi} detik")

print(f"\nTotal waktu: {total_waktu} detik")
