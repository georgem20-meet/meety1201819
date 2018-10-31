class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat (self,food):
		print(" Yummy!! " + self.name + " is eating " +food)
	def description(self):
		print(self.name  + " is " + self.age + " years old and loves the color " + self.favorite_color)



	def make_sound(self):
		print(self.sound)
dog = Animal("woof","John","10","blue")
dog.make_sound()
print(dog.name)
dog.description()
dog.eat(" meat ")

