from heart import Heart


class Berserker(Heart):
    def __init__(self, name: str, attack: float, health_points: int):
        super().__init__(
            name, attack, health_points
        )

    def attack_move_received(self, enemy_attack):
        return self.health_points - enemy_attack
