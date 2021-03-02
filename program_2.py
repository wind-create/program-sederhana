def penjumlahan(a,b):
    return a + b

def pengurangan(a,b):
    return a - b

def perkalian(a,b):
    return a * b

def pembagian(a,b):
    return a / b

while True:
    print("Menu: ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    menu = int(input("pilihan: "))
    if menu == 1:
        a = int(input("masukkan nilai a = "))
        b = int(input("masukkan nilai b = "))
        c = penjumlahan(a,b)
        print(f"Hasil dari penjumlahan a + b = {c}")
    elif menu == 2:
        a = int(input("masukkan nilai a = "))
        b = int(input("masukkan nilai b = "))
        c = pengurangan(a,b)
        print(f"Hasil dari pengurangan a - b = {c}")
    elif menu == 3:
        a = int(input("masukkan nilai a = "))
        b = int(input("masukkan nilai b = "))
        c = perkalian(a,b)
        print(f"Hasil dari perkalian a * b = {c}")
    elif menu == 4:
        a = int(input("masukkan nilai a = "))
        b = int(input("masukkan nilai b = "))
        c = pembagian(a,b)
        print(f"Hasil dari pembagian a / b = {c}")
    else:
        print("tidak ada pilihan")
