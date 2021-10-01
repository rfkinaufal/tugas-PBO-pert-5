class Paus:
    def intro(self):
        print("paus merupakan mamalia terbesar di dunia")

    def deskripsi(self):
        print("paus atau lodan adalah kelompok mamalia yang hidup di lautan")

class orca(Paus):
    def deskripsi(self):
        print("orca atau paus pembunuh merupakan salah satu predator tertinggi di lautan")

class bungkuk(Paus):
    def deskripsi(self):
        print("paus bungkuk adalah paus yang memiliki bentuk tubuh istimewa dengan sirip dada panjang dan kepala menonjol")

obj_paus = Paus()
obj_orca = orca()
obj_bungkuk = bungkuk()

obj_paus.intro()
obj_paus.deskripsi()

obj_orca.intro()
obj_orca.deskripsi()

obj_bungkuk.intro()
obj_bungkuk.deskripsi() 