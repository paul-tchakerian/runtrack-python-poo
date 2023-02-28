class Books:
    def __init__(self, title, author, number_pages):
        self.__title = title
        self.__author = author
        self.__number_pages = number_pages

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

    def display( self ):   # fonction qui permet d' accéder aux attributs pour pouvoir ensuite les print en changeant le nom de l'auteur, du livre et celui du nb de pages
        return f'Titre : {self.__title},Auteur : {self.__author} Nombre de pages : {self.__number_pages}'


BooK001 = Books("Le royaume des Dieux", "Bernard Werber", 485)
BooK001.display()



