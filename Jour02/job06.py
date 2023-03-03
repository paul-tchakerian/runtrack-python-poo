STATUS = ["En attente", "En préparation", "En livraison", "Terminé"]
PLATS = {"Pizza", "Pâtes", "Salade", "Burger", 
        "Sandwich", "Sushi", "Tacos", "Wrap", "Frites", "Boisson"}

TVA= 0.2

class Commande:
        def __init__(self, num_de_commande, list_de_plat_commande, statut = STATUS[0]):
            self.__num_de_commande = num_de_commande
            self.__list_de_plat_commande = list_de_plat_commande
            self.statut = statut

            def ajout_plat(self, plat):
                self.__list_de_plat_commande[plat] = PLATS[plat]
        
            def retirer_plat(self):


            def annuler_commande(self):
                self.statut = STATUS[1]
                self.__list_de_plat_commande = {}

            def calc_prix(self):
                prix = 0
                for plat in self.__list_de_plat_commande:
                    prix += PLATS[plat]
                return prix(1+TVA)

            def pay_commande(self):
                self.statut = STATUS[2]
                self.listes_de_plat_commande = {}

            
            def etat_commande(self):
                return {
                    'num_de_commande': self.__num_de_commande,
                    listes_de_plat_commande: self.__list_de_plat_commande,
                    'statut': self.statut,
                    'prix': self.calc_prix()
                }

            def pretty(d, indent=0):
                for key, value in d.items():
            print('\t' * indent + str(key))
                if isinstance(value, dict):
                    pretty(value, indent+1)
                else:
                   print('\t' * (indent+1) + str(value))


CallCommand = Commande(1, {"Pizza": 10, "Pâtes": 5, "Salade": 5, "Burger": 10, "Sandwich": 5, "Sushi": 10, "Tacos": 5, "Wrap": 5, "Frites": 5, "Boisson": 5}, STATUS[0]) 

print('---STATUT 1---')
priny(pretty(CallCommand.etat_commande()))
