class Kullanici:
    def __init__(self,isim,bakiye):
        self.isim = isim
        self.bakiye = bakiye
        self.portfoy = {}

    def bakiye_goster(self):
        print(f"Kullanici: {self.isim}")
        print(f"Bakiye:{self.bakiye;:.2f} TL")
    
    def portfoy_goster(self):
        if not self.portfoy:
            print("Portfoyunuz bos.")
        else:
            print("Portfoyunuz:")    
            for hisse_kodu, lot in self.portfoy.items():
                print(f"{hisse_kodu}: {lot} lot")
