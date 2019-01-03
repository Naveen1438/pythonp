class bank:

    def assign(self):
        self.name = input ("enter name=")
        self.acno = input("enter acno=")
        self.actype= input("enter accout type")
        global bal
        bal = 500

    def deposit(self):
        global deposit
        deposit = int(input("enter u want deposit="))
    def balance(self):
        global currentbal
        currentbal=bal+deposit
        #print("ur account balance is=",cbalance)

    def withdraw(self):
        global withdraw
        withdraw = int(input("enter u want withdraw="))
        if currentbal >= withdraw:
             print("ur withdraw amount is",withdraw)
        else:
            print("balance inefficient to withdraw")
    def display(self):
        balance=str(currentbal-withdraw)
        print(self.name)
        print("balance=",balance)


b=bank()
b.assign()
b.deposit()
b.balance()
b.withdraw()
b.display()
