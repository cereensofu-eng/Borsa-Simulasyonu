class Hisse:
    def __init__(self, kod, sirket_adi, fiyat):
        self.kod = kod
        self.sirket_adi = sirket_adi
        self.fiyat = fiyat

    def bilgi_goster(self):
        print(f"Hisse Kodu: {self.kod}")
        print(f"Şirket Adı: {self.sirket_adi}")
        print(f"Güncel Fiyat : {self.fiyat:.2f} TL")
        
     