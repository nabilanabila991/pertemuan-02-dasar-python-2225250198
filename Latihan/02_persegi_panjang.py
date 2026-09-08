panjang = float(input("Masukkan panjang (m): "))
lebar = float(input("Masukkan lebar (m): "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print("\n=== HASIL PERHITUNGAN ===")
print(f"Panjang  : {panjang:.2f} m")
print(f"Lebar    : {lebar:.2f} m")
print(f"Luas     : {luas:.2f} m²")
print(f"Keliling : {keliling:.2f} m")
