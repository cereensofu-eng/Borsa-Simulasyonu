import os

def ekran_temizle():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")

def tl_format(fiyat):
    return f"{fiyat:.2f} TL"

def baslik_yaz(baslik):
    print("\n" + "=" * 40)
    print(baslik.center(40))
    print("=" * 40)