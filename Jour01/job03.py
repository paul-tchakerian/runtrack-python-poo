class Operation:
    def __init__( self, nombre1, nombre2 ):
            self.nombre1 = nombre1
            self.nombre2 = nombre2

    def addition( self ):
        return self.nombre1 + self.nombre2


Operation.nombre1 = 45
Operation.nombre2 = 124



print(f'Le nombre1 est {Operation.nombre1}')
print(f'Le nombre2 est {Operation.nombre2}')