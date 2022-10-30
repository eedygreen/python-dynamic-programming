class Vault:
    def __init__(self, gallons=0, litter=0, tanks=0):
        self.gallons = gallons
        self.litter  = litter
        self.tanks   = tanks
    
    def __str__(self) -> str:
        return f"{self.gallons} gallons, {self.litter} litter, {self.tanks} tanks"

    # overloading
    def __add__(self, other):
        gallons = self.gallons + other.gallons
        litter  = self.litter  + other.litter
        tanks   = self.tanks   + other.tanks
        return Vault(gallons, litter, tanks)
    
vault = Vault(20, 80, 0.5)
vault_2 = Vault(40, 160, 3)

print(vault + vault_2)