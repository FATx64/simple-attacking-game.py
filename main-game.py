class hero:
	def __init__(self, name, attackPower, HealthPoint, Armor):
		self.name = name
		self.attackPower = attackPower
		self.HealthPoint = HealthPoint
		self.Armor = Armor

	def attacking(self, enemy):
		print(self.name, "attacking" ,enemy.name)
		enemy.defend(self, self.attackPower)

	def defend(self, enemy, enemyDMG):
		print(self.name, "attacking by", enemy.name)
		damage = enemyDMG/self.Armor
		print("DMG = ", str(damage))
		self.HealthPoint -= damage
		print("HP = ", self.name, "remaining HP", str(self.HealthPoint))




hero1 = hero("klee",200,150,100)
hero2 = hero("traveler", 250,110,50)

print(hero1.__dict__)
hero1.attacking(hero2)
print("\n")
print(hero2.__dict__)
hero2.attacking(hero1)
print("\n")
print(hero1.__dict__)
hero1.attacking(hero2)
print("\n")
print(hero2.__dict__)
hero2.attacking(hero1)
print("\n")
print(hero1.__dict__)
hero1.attacking(hero2)
print("\n")
print(hero2.__dict__)
hero2.attacking(hero1)
print("\n")
print(hero1.__dict__)
hero1.attacking(hero2)
print("\n")
print(hero2.__dict__)
hero2.attacking(hero1)
