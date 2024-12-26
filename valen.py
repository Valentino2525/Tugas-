from abc import ABC, abstractmethod

# Abstract class
class Kendaraan(ABC):
    @abstractmethod
    def jumlah_roda(self):
        pass

    @abstractmethod
    def bahan_bakar(self):
        pass

    @abstractmethod
    def kapasitas_penumpang(self):
        pass

# Implementasi class abstrak
class Mobil(Kendaraan):
    def jumlah_roda(self):
        return 4

    def bahan_bakar(self):
        return "Bensin"

    def kapasitas_penumpang(self):
        return 5

class Motor(Kendaraan):
    def jumlah_roda(self):
        return 2

    def bahan_bakar(self):
        return "Bensin"

    def kapasitas_penumpang(self):
        return 2

class Sepeda(Kendaraan):
    def jumlah_roda(self):
        return 2

    def bahan_bakar(self):
        return "Tidak menggunakan bahan bakar"

    def kapasitas_penumpang(self):
        return 1

# Penggunaan
mobil = Mobil()
motor = Motor()
sepeda = Sepeda()

print(f"Mobil: {mobil.jumlah_roda()} roda, bahan bakar {mobil.bahan_bakar()}, kapasitas {mobil.kapasitas_penumpang()} orang.")
print(f"Motor: {motor.jumlah_roda()} roda, bahan bakar {motor.bahan_bakar()}, kapasitas {motor.kapasitas_penumpang()} orang.")
print(f"Sepeda: {sepeda.jumlah_roda()} roda, bahan bakar {sepeda.bahan_bakar()}, kapasitas {sepeda.kapasitas_penumpang()} orang.")
