import random 
from hisse import Hisse

class Borsa:
    def __init__(self):
        self.hisseler = []

        self.hisse_ekle("THYAO", "Türk Hava Yolları", 325.50)
        self.hisse_ekle("ASELS", "Aselsan", 142.75)
        self.hisse_ekle("TUPRS", "Tüpraş", 188.20)
        self.hisse_ekle("KCHOL", "Koç Holding", 210.40)
        self.hisse_ekle("SISE", "Şişecam", 48.90)
        self.hisse_ekle("BIMAS", "BİM", 615.30)
        self.hisse_ekle("GARAN", "Garanti BBVA", 135.60)
        self.hisse_ekle("AKBNK", "Akbank", 72.40)
    
    def hisse_ekle(self,kod, sirket_adi, fiyat):
        yeni_hisse = Hisse(kod,sirket_adi, fiyat)
        self.hisseler.append(yeni_hisse)

    def hisseleri_listele(self):
        print("\n----- BORSA -----")
        
        for hisse in self.hisseler:
            print(f"{hisse.kod} | {hisse.sirket_adi} | {hisse.fiyat:.2f} TL")
    
    def hisse_bul(self, kod):
        for hisse in self.hisseler:
            if hisse.kod == kod:
                return hisse
        return None
    
    def fiyat_guncelle(self):
        for hisse in self.hisseler:
            degisim = random.uniform(-0.05, 0.05)
            hisse.fiyat += hisse.fiyat * degisim

            if hisse.fiyat < 1:
                hisse.fiyat = 1
        print("Hisse fiyatları güncellendi.")
         
