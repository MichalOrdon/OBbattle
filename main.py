from berserker import Berserker
from gladiator import Gladiator

berserker = Berserker("Greg", 12, 4.4, 1)
gladiator = Gladiator("Gunter", 19, 2.5, 1)


print(berserker)
print(gladiator)
berserker.attack_move_received(gladiator.strenght)
print(berserker)
berserker.defense_pose()
print(berserker)
berserker.hp_potion_usage()
print(berserker)
berserker.amok()
print(berserker)
gladiator.attack_move_received(berserker.special_attack())
print(gladiator)
