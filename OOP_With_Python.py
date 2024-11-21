
class dog:
    #class attribute
    species="Canis familiaris"
    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed
        
    def __str__(self):
        return(f"{self.name} is a {self.age} year old {self.breed}")
    
    def noise(self,sound):
        return(f"{self.name} says {sound}")
Cindy=dog('Cindy',5,'jack russel terrier')
lola=dog('lola',3.5,'golden retriever')
lola.breed
'golden retriever'
lola.species
'Canis familiaris'
lola.age
3.5
lola.age = 4
lola.age
4
class Doggy:
    species= 'Draconis Maplefeist'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def noise(self,sound):
        return f"{self.name} makes a {sound} noise"
BobaFett=Doggy('BobaFett',8)
BobaFett.noise('barking')
'BobaFett makes a barking noise'
# using '__str__' instead of 'description'
class Doggy:
    species= 'Draconis Maplefeist'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def noise(self,sound):
        return f"{self.name} makes a {sound} noise"
Murife=Doggy('Murife',2)
print(Murife)
Murife is 2 years old
class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
        
    def __str__(self):
        return f"My {self.color} car has {self.mileage} miles"
#a blue car with 20,000 miles and a red car with 30,000 miles
Eleanor = Car('Blue',20000)
print(Eleanor)
My Blue car has 20000 miles
Ares = Car('Red',30000)
print(Ares)
My Red car has 30000 miles
for car in (Eleanor, Ares):
    print(f"My {car.color} has {car.mileage:,} miles")
#the comma separes the numerics by the thousands
My Blue has 20,000 miles
My Red has 30,000 miles
Mylo = dog('Mylo',11,'Dashlund')
Kiki = dog('Kiki',1,'Chihuahua')
Spike = dog('Spike',6,'Bulldog')
Tommy = dog('Tommy',6,'Bulldog')
Mylo.noise('Yap')
'Mylo says Yap'
class Dashlund(Doggy):
    pass
class Chihuahua(Doggy):
    pass
class Bulldog(Doggy):
    pass
Joseph=Dashlund('Joseph',7) 
print(Joseph)
Joseph is 7 years old
type(Joseph)
__main__.Dashlund
class Dashlund(Doggy):
    def noise(self,sound='Arggg'):
        return super().noise(sound)
Penelope=Dashlund('Penelope',3)
print(Penelope)
Penelope is 3 years old
Penelope.noise()
'Penelope makes a Arggg noise'
class GoldenRetriever(Doggy):
    def noise(self,sound='Bark'):
        return super().noise(sound)
Luka=GoldenRetriever('Luka',0.5)
print(Luka)
Luka is 0.5 years old
Luka.noise()
'Luka makes a Bark noise'
class test:
    def __init__(self):
        print('I came here without your permission lol')
print(test())
I came here without your permission lol
<__main__.test object at 0x000001B0B4A90D90>
