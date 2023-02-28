class Characters:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_right( self ):
        self.x -= 1

    def move_left( self ):
        self.x += 1

    def move_up( self ):
        self.y += 1

    def move_down( self ):
        self.y -= 1

    def display_position( self):
        return f'abscisse={self.x}, ordonnée={self.y}'

character = Characters(0,0)

print(f'The character is in position {character.display_position()}')

character.move_right()
character.move_right()
character.move_right()
print(f'The character is in position {character.display_position()}')
character.move_down()
character.move_down()
character.move_down()
print(f'The character is in position {character.display_position()}')
character.move_left()
character.move_left()
character.move_left()
print(f'Le personnage est en position {character.display_position()}')
character.move_up()
character.move_up()
character.move_up()
print(f'Le personnage est en position {character.display_position()}')
