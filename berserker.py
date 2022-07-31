from heart import Heart


class Berserker(Heart):
    def __init__(self, name: str, health_points: float, strenght: float, defense_points: int = 1):
        super().__init__(
            name, health_points, strenght, defense_points
        )

    def attack_move_received(self, enemy_attack):
        self.health_points -= enemy_attack / self.defense_points

    def defense_pose(self):
        self.defense_points += 4

    def amok(self):  # umiejętność klasowa
        self.health_points *= 0.5
        self.strenght *= 1.5

    def special_attack(self):  #klasowy atak specjalny
        deald_damage = self.strenght * 2
        return deald_damage
