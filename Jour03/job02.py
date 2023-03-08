class BankAccount:
    def __init__(self, number, name, firstname, balance, overdraft):
        self.accuont_number = number
        self.__name = name
        self.__balance = balance
        self.__firstname = firstname
        self.__balance = balance
        self.__overdraft = overdraft

    def show_infos(self):
        print (f" Nom: {self.__name}  Prénom: {self.__firstname} Solde : {self.__balance} "
                f"Prénom: {self.__firstname} Nom: {self.__lastname} Solde: {self.__balance} ")

    def show_balance(self): 
        print(f"Solde: {self.__balance}")

    def remittance(self):  
        print("Le solde du compte bancaire de", self.nom, "est de", self.solde, "euros.")


    def withdraw_money(self, amount):
        if amount > self.__balance or self.__overdraft:
            print("Le solde du compte bancaire de", self.nom, "est de", self.solde, "euros.")
            if amount <= self.__balance < 0:
                self.__balance -= amount
                print(f"Le retrait à été éffectué avec succés. {amount} $")
            else: 
                print(f"Pas assez d'argent sur le compte. Le solde actuel est de : {self.__balance} euros.")
        else:
            print("Erreur")

    def agios(self):
        if self.__balance < 0:
            self.__balance -= 12
            print(f"Vous avez dépassé votre découvert autorisé. Vous avez été débité de 20 euros. Votre solde est de {self.__balance} euros.")
        else:
            print("Vous n'avez pas dépassé votre découvert autorisé.")


    def bank_transfer(self, amount, account):
        if amount <= self.__balance  or self.__overdraft:
            self.__balance -= amount
            account.receive_money(amount, self.__name)
            print(f"Le virement à été éffectué avec succés. {amount} ")
        if self.__balance < 0:
            self.apply_bank_fees()

    def receive_money_(self, amount, name):
        self.__balance += amount
        print(f"Le dépôt de {amount} à été éffectué avec succés sur votre compte depuis le compte de Mr.{name}")

    def apply_bank_fees(self):
        fees =- self.__balance * (7/100)
        self.__balance -= fees
        print(f"Les redevences s'élévent à {fees} euros. Votre solde est de {self.__balance} euros.")


bank_account01 = BankAccount(123456789, "Barack", "Obama", 10000, True)
bank_account02 = BankAccount(987654321, "Donald", "Trump", 10000, True)


print(bank_account01.show_infos())
print(bank_account02.show_infos())
bank_account01.remittance(bank_account02, 20)
