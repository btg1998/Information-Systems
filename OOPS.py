class BTG_Bank:
    """ This is the class for the Bank """
    def __init__(self,c_name,a_no,a_type,bal):
        self.name=c_name
        self.an=a_no
        self.type=a_type
        self.balance=bal
    def deposit(self, amt):
        self.balance=self.balance+amt
    def withdraw(self, amt):
        if amt>self.balance:
            print("Sorry..not enough Money... :-(")
        else:
            self.balance=self.balance-amt
    def balance1(self):
        print("Balance: ",self.balance)
    def full(self):
        print(" Customer Name: "+str(self.name))
        print(" Account Number: "+str(self.an))
        print(" Account Type: "+str(self.type))
        print(" Balance: "+str(self.balance))
class Bank(BTG_Bank):
    def __init__(self,c_name,a_no,a_type,bal):
        BTG_Bank.__init__(self,c_name,a_no,a_type,bal)
    def cinterest(self,rate):
        int1=(self.balance*rate*0.5)/100
        return int1
Var=BTG_Bank("Arun",10001,"Current",1000000)
Var1=Bank("Arun",10001,"Current",1000000)
Var1.full()
ch='y'
while(ch=='y'):
    print("Choose Your Choice")
    n=int(input("1) Deposit\n 2)withdraw\n 3)Display Balance\n 4)Display with full details\n 5)Exit\n 6)Interest on fixed deposit for 6 months\n 7)Choose"))
    if n==5:
        ch='n'
    if n==6:
        try:
            r=float(input(("Enter the interest Rate: ")))
            print(Var1.cinterest(r))
        except:
            print("-_- Not a number.")
        
    if n==7:
        continue
    if n==1:
        try:
            a=float(input("Enter the amount to be deposited: "))
            Var1.deposit(a)
        except ValueError:
            print("-_- Not a number.")
    if n==2:
        try:
            a=float(input("Enter the amount to be withdrawn: "))
            Var1.withdraw(a)
        except ValueError:
              print("-_- Not a number.")
              
    if n==3:
        Var1.balance1()
    if n==4:
        Var1.full()
