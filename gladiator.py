from heart import Heart


class Gladiator(Heart):
    def __init__(self, name: str, health_points: float, strenght: float, defense_points: int = 1):
        super().__init__(
            name, health_points, strenght, defense_points
        )

    def attack_move_received(self, enemy_attack):
        self.health_points -= enemy_attack / self.defense_points
