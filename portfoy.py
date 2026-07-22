class Portfoy:
    def __init__(self):
        self.bakiye = 100000
        self.hisseler ={}

    def hisse_al(self, hisse, adet, fiyat):
        maliyet = adet * fiyat
        
        if maliyet <= self.bakiye:
            self.bakiye -= maliyet

            if hisse in self.hisseler:
                self.hisseler[hisse] += adet
            else:
                self.hisseler[hisse] = adet

            print(f"{adet} adet {hisse} satin alindi.")
        else:
            print("Yetersiz bakiye!")
    def hisse_sat(self, hisse, adet,fiyat):
        if hisse in self.hisseler and self.hisseler[hisse]>= adet:

            self.hisseler[hisse] -= adet
            self.bakiye += adet * fiyat 

            if self.hisseler[hisse]==0:
                del self.hisseler[hisse]
            print(f"{adet} adet {hisse} satildi.")
        else:
            print("Yeterli hisse yok!")
    def portfoy_goster(self):
        print("\n----- PORTFOY-----")
        print(f"Bakiye: {self.bakiye:.2f} tl")
        if len(self.hisseler)== 0:
            print("Portfoy boş.")
        else:
            for hisse, adet in self.hisseler.items():
                print(f"{hisse}: {adet} adet")
  

                
