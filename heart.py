class Heart:
    def __init__(self, name: str, health_points: float, strenght: float, defense_points: int):
        self.__name = name
        self.health_points = health_points
        self.strenght = strenght
        self.defense_points = defense_points

        assert strenght >= 0, f"Moc ataku nie może być ujemna. {strenght}"

    def __repr__(self):
        return f"Imię: {self.__name}, życie: {self.health_points}, siła: {self.strenght}, obrona: {self.defense_points}"

    @property  # getter, Imie można nadać tylko raz!
    def name(self):
        return self.__name

    @name.setter    # setter, Chrzest imienia; Nadanie pierwszego imienia
    def name(self, nowe_imie):
        self.__name = nowe_imie

    def hp_potion_usage(self):
        self.health_points += 10
