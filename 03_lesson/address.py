class Address:

    def __init__(self, postcode, city, street, building, appartment):
        self.Postcode = postcode
        self.City = city
        self.Street = street
        self.Building = building
        self.Appartment = appartment

    def __str__(self):
        return f"{self.Postcode}, {self.City}, {self.Street}, " \
            f"{self.Building} - {self.Appartment}"