class Person:
    def __init__(self, surname, first_name):
        self.first_name = first_name
        self.surname = surname


    def IntroduceYourSelf ( self ):
        '''Se présenter en anglais se traduit littéralement par Introduce your self'''
        
        return f'Je suis {self.first_name} {self.surname}'

print(Person.SePresenter(Person('John', 'Doe')))

print(Person.SePresenter(Person('Jean', 'Dupont')))