
class Point:

     def __init__( self, x, y ):
           self.x = x
           self.y = y
     def display_the_points( self ):
         return f'Le point est ({self.x} , {self.y})'

     def display___x( self ):
         return f'Le point  x est ({self.x})'

     def display___y( self ):
         return f'Le point y est ({self.y})'

     def changeX( self, x ):
         self.x = x

     def changeY( self, y ):
         self.y = y

point = Point ( 68,89 )

print(f'Le point est afficher {point.display_the_points()}')
print(f'Le point x est affiché {point.display___x()}')
print(f'Le point x est affiché {point.display___y()}')
print(f'Le point y est changé{point.changeX(68)}')
print(f' Le point y esst changé{point.changeY(89)}')
print(f'Le point est affiché {point.display_the_points()}')
