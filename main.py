class Heart:
    def __init__(self, name: str, attack: float, health_points: int):
        self.__name = name
        self.attack = attack
        self.health_points = health_points

        assert attack <= 0, f"Moc ataku nie może być ujemna."

    @property  # getter, Imie można nadać tylko raz!
    def name(self):
        return self.__name

    @name.setter    # setter, Chrzest imienia; Nadanie pierwszego imienia
    def name(self, nowe_imie):
        self.__name = nowe_imie
