#init
class Peoples:
    def __init__(self, name, age):
        self.name = name
        self.age = age

result = Peoples("Dima", 18)
print(result.name)  
print(result.age)

#str
class Peoples:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

result = Peoples("Dmitrii", 16 )
print(result) 

#call
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

doubler = Multiplier(2)
result = doubler(5) 
print(result)  

