# Class 
class Televisi:
    # Constructor
    def __init__(self, pd):
        self.Type = ""
        self.Merk = ""
        self.pd = pd

    # Method to print television information
    def printTV(self):
        print("Type Televisi : ", self.Type)
        print("Merk Televisi : ", self.Merk)
        print("Produk : ", self.pd)
    
    # Method to indicate setting completion
    def Her(self, kondisi):
        print("Telah disetting untuk digunakan")
        print(kondisi)

# Objects
TV1 = Televisi("Digital")
TV2 = Televisi("Elektronik")

# Set values
TV1.Type = "Digital"
TV1.Merk = "Samsung"
TV2.Type = "Analog"
TV2.Merk = "Mito"

# Call methods
TV2.printTV()
TV2.Her("Uji coba televisi yang sudah disetting")
