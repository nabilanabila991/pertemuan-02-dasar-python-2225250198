import math

print("=== Kalkulator Koordinat ===")

x1 = float(input("Masukkan x1: "))
y1 = float(input("Masukkan y1: "))

x2 = float(input("Masukkan x2: "))
y2 = float(input("Masukkan y2: "))

jarak = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"\nTitik A = ({x1}, {y1})")
print(f"Titik B = ({x2}, {y2})")
print(f"Jarak A ke B = {jarak:.2f}")
