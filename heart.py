class Heart:
    def __init__(self, name: str, attack: float, health_points: int):
        self.__name = name
        self.attack = attack
        self.health_points = health_points

        assert attack >= 0, f"Moc ataku nie może być ujemna. {attack}"

    def __repr__(self):
        return f"Imię: {self.__name}, siła: {self.attack}, życie: {self.health_points}"

    @property  # getter, Imie można nadać tylko raz!
    def name(self):
        return self.__name

    @name.setter    # setter, Chrzest imienia; Nadanie pierwszego imienia
    def name(self, nowe_imie):
        self.__name = nowe_imie
