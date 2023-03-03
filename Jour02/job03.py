class Books:
    def __init__(self, title, author, number_pages):
        self.__title = title
        self.__author = author
        self.__number_pages = number_pages
        self._available = True

    def set_attributes( self, title, author, number_pages):
        if self.__number_pages > 0 and type(self.__number_pages)==int:
            self.__title = title
            self.__author = author
            self.__number_pages = number_pages

    def get_number_pages(self):
        return self.__number_pages

    def set_number_pages( self, number_pages ):
        if isinstance(number_pages, int) and number_pages >= 0:
            self.__number_pages = number_pages
        else:
            print("Erreur: le nombre de pages doit être un entier positif ! ")

    def check(self):
        return self._available

    def borrow(self):
        if self.check():
            self._available = False
            return "Livre emprunté"
        else:
                return "Livre non disponible"
    
    def render(self):
        if not self.check():
            self._available = True
        else:
                return"Livre déja rendu"

    def is_available(self):
        if self._available:
                return "Livre disponible" 
        else:
                return "Livre non disponible"     

    def display_attributes( self ):   # fonction qui permet d' accéder aux attributs pour pouvoir ensuite  print ces derniers en changeant le nom de l'auteur, du livre et celui du nb de pages
        return f'Titre : {self.__title}Auteur : {self.__author} Nombre de pages : {self.__number_pages}'
    

Books._available = True

BooK001 = Books("Le royaume des Dieux", "Bernard Werber", 485)
print(BooK001.display_attributes())

BooK001.set_attributes("Le royaume des Dieux", "Bernard Werber", 270)
print(BooK001.display_attributes())
print(BooK001.borrow())
print(BooK001.is_available())
print(BooK001.render())
print(BooK001.is_available())