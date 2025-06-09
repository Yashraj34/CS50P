import random

class Hat:
    houses=["Gryffindor","Slytherin","Ravenclaw","hufflepuff"]

    @classmethod
    def sort(cls,name):
        print(name,"is in", random.choice(cls.houses))

Hat.sort("Harry")
