class Car:
    def __init__(self, brand, model, year, mileage, en_marche = False, container = 50):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__en_marche = en_marche
        self.__container = container

    def start(self):
        if self.__en_marche == True: 
            return "La voiture est en marche"
        elif self.__container >= 3:
            self.__container > 3 
            return "La voiture est déjà en marche"
        elif self.__container < 3:
            return "La voiture n'a pas assez d'essence pour démarrer"
        
    def stop(self):
        if self.__en_marche == False:
            return "La voiture est déjà arrêtée"
        else:
            return "La voiture est arrêtée"
        
    def check_conainer(self):
        return f"Le réservoir contient {self.__container} litres d'essence"


car_1 = Car("Seat""Leon", 2018, 0, 190.964)

print(car_1.start())
