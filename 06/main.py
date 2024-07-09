class Mashina:
    def __init__(self, nomi, turi, ishlab_chiqarilgan_yili, narxi=4000):
        self.nomi = nomi
        self.turi = turi
        self.narxi = narxi
        self.ishlab_chiqarilgan_yili = ishlab_chiqarilgan_yili

    def malumot(self):
        return (f"Mashina nomi: {self.nomi}, "
                f"Turi: {self.turi}, "
                f"Narxi: ${self.narxi}, "
                f"Ishlab chiqarilgan yili: {self.ishlab_chiqarilgan_yili}")


mashinalar = []
for i in range(5):
    print(f"\n{i + 1}-mashina ma'lumotlarini kiriting:")
    nomi = input("Mashina nomi: ")
    turi = input("Mashina turi (yengil, yuk avtomobili): ")
    ishlab_chiqarilgan_yili = int(input("Ishlab chiqarilgan yili: "))
    narx = input("Narxi (bo'sh qoldirilsa default $4000 bo'ladi): ")

    if narx:
        narx = int(narx)
        mashina = Mashina(nomi, turi, ishlab_chiqarilgan_yili, narx)
    else:
        mashina = Mashina(nomi, turi, ishlab_chiqarilgan_yili)

    mashinalar.append(mashina)

mashinalar.sort(key=lambda x: x.ishlab_chiqarilgan_yili)

print("\nMashinalar ishlab chiqarilgan yili bo'yicha saralangan holda:")
for mashina in mashinalar:
    print(mashina.malumot())
