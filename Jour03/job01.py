

class City:
    def __init__(self, name, number):
        self.__city_name = name
        self.__population = number
        print(f"Population of {self.__city_name} is: {self.__population}")


    def add_new_population(self):
        self.__population += 1
        self.__population


class People:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def add_to_population(self):
        self.__population.add_new_population()


Cityy01 = City("Paris", 4000000)
Cityy02 =City("Marseille",  861635)


Human_0 = People("Jhon", 45, Cityy01)
Human_1 = People("Myrtille", 4, Cityy01)
Human_2 = People("Chloé", 45, Cityy02)

Human_0.add_to_population()
Human_1.add_to_population()
Human_2.add_to_population()

print(Cityy01.__population)
print(Cityy02.__population)

print(f"Population of is: {Cityy01.update_population()}")
print(f"Population of is {Cityy02.update_population()}")

