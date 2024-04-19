# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:00:43 2024

@author: kusfi
"""

class Masyarakatkampus:
    def __init__(self, nama):
        self.nama = nama

    def Gaji(self):
        pass

class Dosen(Masyarakatkampus):
    def __init__(self):
        super().__init__("Dosen")

    def Gaji(self):
        return "Golongan Dosen mendapatkan gaji", "45000"

class Karyawan(Masyarakatkampus):
    def __init__(self):
        super().__init__("STAFF")

    def Gaji(self):
        return "Golongan STAFF mendapatkan gaji", "30000"

class Lain(Masyarakatkampus):
    def __init__(self):
        super().__init__("Lain")

    def Gaji(self):
        return "Golongan Lain mendapatkan gaji", "150000"

def main():
    dosen = Dosen()
    karyawan = Karyawan()
    lain = Lain()

    print(dosen.nama)
    print(dosen.Gaji())
    print(karyawan.nama)
    print(karyawan.Gaji())
    print(lain.nama)
    print(lain.Gaji())

if __name__ == "__main__":
    main()