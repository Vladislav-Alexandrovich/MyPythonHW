from smartphone import Smartphone

catalog = [
    Smartphone("IPhone", "10", "+7123456789"),
    Smartphone("Motorola", "7", "+7987654321"),
    Smartphone("Samsung", "8", "+7123459876"),
    Smartphone("Nokia", "5", "+7987612345"),
    Smartphone("LG", "6", "+7567891234")
]

for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model}, {Smartphone.number}")
