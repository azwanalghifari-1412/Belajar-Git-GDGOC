import random

# Variabel
angka_rahasia = random.randint(1, 10)

# Perulangan
for i in range(3):
    tebakan = int(input("Tebak angka (1-10): "))

    # Percabangan
    if tebakan == angka_rahasia:
        print("Selamat! Tebakan kamu benar 🎉")
        break
    elif tebakan < angka_rahasia:
        print("Terlalu kecil!")
    else:
        print("Terlalu besar!")
else:
    print(f"Maaf, kamu kalah. Angkanya adalah {angka_rahasia}")
