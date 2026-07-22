from borsa import Borsa
from portfoy import Portfoy

class Islemler:
    def __init__(self):
        self.borsa= Borsa()
        self.portfoy= Portfoy()

    def menu(self):
        while True:
            print("\n====== PYTHON BORSA SİMÜLASYONU ======")
            print("1 - Hisse Fiyatlarını Göster")
            print("2 - Hisse Al")
            print("3 - Hisse Sat")
            print("4 - Portföyü Göster")
            print("5 - Fiyatları Güncelle")
            print("0 - Çıkış")

            secim = input("Seçiminiz: ")

            if secim == "1":
                self.borsa.hisseleri_listele()

            elif secim =="2":
                hisse = input("Hisse Kodu: ").upper()
                adet = int(input("Kaç adet: "))
                bulunan_hisse = self.borsa.hisse_bul(hisse)
                if bulunan_hisse is None:
                    print("Hisse bulunamadı!")
                    continue
                fiyat = bulunan_hisse.fiyat
                self.portfoy.hisse_al(hisse, adet, fiyat)
            elif secim =="3":
                hisse = input("Hisse Kodu:  ").upper()
                adet = int(input("Kaç adet:  "))
                bulunan_hisse = self.borsa.hisse_bul(hisse)
                if bulunan_hisse is None:
                    print("Hisse bulunamadı!")
                    continue
                fiyat=bulunan_hisse.fiyat
                self.portfoy.hisse_sat(hisse, adet, fiyat)
            elif secim =="4":
                self.portfoy.portfoy_goster()
            elif secim =="5":
                self.borsa.fiyat_guncelle()
            elif secim =="0":
                print("Programdan çıkılıyor...")
                break
            else:
                print("Geçersiz seçim!")