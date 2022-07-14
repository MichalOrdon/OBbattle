from berserker import Berserker
from gladiator import Gladiator

berserker = Berserker("Greg", 9.4, 12)
gladiator = Gladiator("Gunter", 5.5, 19)

print(berserker.attack_move_received(gladiator.attack))
