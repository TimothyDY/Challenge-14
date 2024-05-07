import Python.Meet24.Fisika.pycache as pycache
import time
import Fisika.JualBeli

def batas():
    print("-"*15)
    
waktu_awal = time.time()
print(f"Massa Jenis = {pycache.MassaJenis.MassaJenis(10,2)}")
print(f"Massa = {pycache.MassaJenis.Massa(10,2)}")
print(f"Volume = {pycache.MassaJenis.Volume(10,2)}")

waktu_akhir = time.time()
print(f"waktu yang dibutuhkan : {waktu_akhir - waktu_awal}")

batas()
print(f"Usaha = {pycache.U(12,3)}")
print(f"Usaha = {pycache.G(6,2)}")
print(f"Usaha = {pycache.J(10,2)}")

batas()

print(f" Hasil Energi Potensial : {pycache.Ep(4,7,4)}")
print(f"Hasil Energi Kinetik : {pycache.Ek(4, 7)}")
batas()

diskon10 = pycache.jl(10)
result = diskon10(10000)
print(f"Diskon 10% = {result}")