import itertools

def jadwalkan_lampu_lalu_lintas(jalur):
    
    durasi_max = max (jalur.values())
    durasi = list(range(1, durasi_max + 1))
    
    kombinasi_terbaik = None
    total_waktu_min = float ('inf')
    
    for kombinasi in itertools.product (durasi,repeat=len(jalur)):
        total_waktu = sum (kombinasi)
        if total_waktu < total_waktu_min:
            total_waktu_min = total_waktu
            kombinasi_terbaik = kombinasi
    return list(zip(jalur.keys(), kombinasi_terbaik)), total_waktu_min
            
jalur = {
    'A': 30,
    'B': 50,
    'C': 20,
    'D': 40
}
    
jadwal, total_waktu = jadwalkan_lampu_lalu_lintas(jalur)

for green_time in jadwal:
    print(f"{green_time[1]}detik")
    
print(f"\n{total_waktu}detik")