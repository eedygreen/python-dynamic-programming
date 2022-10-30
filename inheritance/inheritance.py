class Scholar:
    def __init__(self, name):
        if not name:
            raise ValueError(f"{name} not defined")
        self.name = name

class Talib(Scholar):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

class Duktoor(Scholar):
    def __init__(self, name, faculty):
        super().__init__(name)
        self.faculty = faculty

scholar = Scholar("Ibn Taimiya")
talib   = Talib("Eedy", "Ulum ul Qur'an")
duktoor = Duktoor("Ibn Uthaymeen", "Tafseer")
