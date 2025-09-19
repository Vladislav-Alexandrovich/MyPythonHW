from address import Address


class Mailing:

    def __init__(self, from_address, to_address, cost, track):
        self.From_address = from_address
        self.To_address = to_address
        self.Cost = cost
        self.Track = track

    def __str__(self):
        return f"Отправление {self.Track} из {self.From_address}" \
               f" в {self.To_address}. Cтоимость {self.Cost} рублей."

