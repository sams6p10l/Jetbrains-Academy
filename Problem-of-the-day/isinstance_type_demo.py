'''
OOP: Inheritance in Python
Which type checks will return True? 
'''


class Plant:
    def __init__(self, spec):
        self.spec = spec


class Cactus(Plant):
    pass


basil = Plant("Ocimum basilicum")

opuntia = Cactus("Opuntia vulgaris")


print(isinstance(basil, Plant))
print(type(opuntia) == Cactus)
print(type(basil) == Cactus)
print(isinstance(opuntia, Plant))
print(type(basil) == object)
print(type(opuntia) == Plant)
print(isinstance(opuntia, object))


'''
    isinstance(basil, Plant):
        basil is an instance of Plant, so this check will return True.

    type(opuntia) == Cactus:
        The type of opuntia is Cactus, as it is created as an instance of the Cactus class. This check will return True.

    type(basil) == Cactus:
        basil is an instance of the Plant class, not the Cactus class. This check will return False.

    isinstance(opuntia, Plant):
        opuntia is an instance of Cactus, which is a subclass of Plant. Therefore, opuntia is also an instance of Plant. This check will return True.

    type(basil) == object:
        The type() function directly compares the type of an object. Since basil is an instance of the Plant class, its type is Plant, not object. This check will return False.

    type(opuntia) == Plant:
        The type() function checks for the exact class, and since opuntia is an instance of the Cactus class, not the Plant class directly, this check will return False.

    isinstance(opuntia, object):
        All Python objects are instances of the base class object. Therefore, this check will return True.

Correct Answers:

    isinstance(basil, Plant)
    type(opuntia) == Cactus
    isinstance(opuntia, Plant)
    isinstance(opuntia, object)

'''
