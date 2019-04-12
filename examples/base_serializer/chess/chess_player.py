from datetime import date


class ChessPlayer:

    def __init__(self, email: str, birth_date: date, pesel: str, rodo_accepted: bool):
        self.email = email
        self.birth_date = birth_date
        self.pesel = pesel
        self.rodo_accepted = rodo_accepted

