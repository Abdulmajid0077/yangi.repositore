users = ['Salom', 'Hello']
print(users[0])

#---------

def say_hello(name: str):
    return f"Assalomu alaykum {name}"

print(say_hello("Abdulmajid"))

#----------

class Car:
    def __init__(self, model: str, bradn: str, price: int, color:str):
        self.model = model
        self.brand = bradn
        self.price = price
        self.color = color

    def to_dict(self):
       return self.__dict__
    
print("Bu faylda ish tugadi !!!")

print("Davomi bor")