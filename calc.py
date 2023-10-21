# Fungsi untuk penjumlahan
def add(x, y):
    return x + y

# Fungsi untuk pengurangan
def subtract(x, y):
    return x - y

# Fungsi untuk perkalian
def multiply(x, y):
    return x * y

# Fungsi untuk pembagian
def divide(x, y):
    if y == 0:
        return "Tidak bisa membagi dengan nol"
    return x / y

# Fungsi untuk akar kuadrat
def square_root(x):
    if x < 0:
        return "Angka harus positif"
    return x ** 0.5

# Fungsi untuk perpangkatan
def power(x, y):
    return x ** y

# Fungsi untuk operasi modulus
def modulus(x, y):
    return x % y

while True:
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Akar Kuadrat")
    print("6. Perpangkatan")
    print("7. Modulus")
    print("8. Keluar")

    choice = input("Masukkan pilihan (1/2/3/4/5/6/7/8): ")

    if choice == '8':
        print("Keluar dari kalkulator.")
        break

    if choice not in ('1', '2', '3', '4', '5', '6', '7'):
        print("Pilihan tidak valid")
        continue

    num1 = float(input("Masukkan angka pertama: "))
    if choice != '5':
        num2 = float(input("Masukkan angka kedua: "))

    if choice == '1':
        print("Hasil:", add(num1, num2))
    elif choice == '2':
        print("Hasil:", subtract(num1, num2))
    elif choice == '3':
        print("Hasil:", multiply(num1, num2))
    elif choice == '4':
        print("Hasil:", divide(num1, num2))
    elif choice == '5':
        print("Hasil:", square_root(num1))
    elif choice == '6':
        print("Hasil:", power(num1, num2))
    elif choice == '7':
        print("Hasil:", modulus(num1, num2))
