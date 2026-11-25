class Murabiy:
    def __init__(self,ism,sport):
        self.ism = ism
        self.sport = sport

    def malumot(self):
        return f"{self.ism} - {self.sport}"


class Sportchi:
    def __init__(self,ism,yosh,murabiy:Murabiy):
        self.ism = ism
        self.yosh = yosh
        self.murabiy = murabiy

    def malumot(self):
        print(f"{self.ism} ({self.yosh} yosh) - murabiy: {self.murabiy.ism} ({self.murabiy.sport})")

    def saqlash(self):
        with open("sportchilar.txt","a") as f:
            f.write(f"{self.ism} - {self.yosh} yoshda\n")

m1 = Murabiy("Pep Guardiola", "Futbol")
m2 = Murabiy("Steve Kerr", "Basketbol")

s1 = Sportchi("Abduqodir", 22, m1)
s2 = Sportchi("Haaland", 24, m1)
s3 = Sportchi("Stephen Curry", 36, m2)
s4 = Sportchi("Jayson Tatum", 26, m2)

sportchilar = [s1,s2,s3,s4]
for s in sportchilar:
    s.saqlash()

s1.malumot()
s2.malumot()
s3.malumot()
s4.malumot()


