class Rectangle:
     def __init__(self, length, width ):
         self.__length = length
         self.__width = width

     def set_length(self, length):  # j' utilises la méthode "set" pour modifier les attrib. privées du rectangle
         return self.__length

     def set_width(self, width):
        return self.__width

     def get_length(self):    # j' utilises cette-fois-ci la méthode "get" pour accéder
                                # à ses attrib. qui sont pour l'occurrence "lenght" et "width"
        return self.__length

     def get_width(self):
        return  self.__width


     def print_attributes( self):
            return f'Length: {self.__length} Width: {self.__width}'


Rect_dimensions = Rectangle(10, 20)
print(Rect_dimensions.print_attributes())

Rect_dimensions.set_length(47)
Rect_dimensions.set_width(24)
print({Rect_dimensions.print_attributes()})