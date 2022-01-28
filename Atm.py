class Atm :
    def __init__(self,atm_number,atm_pin):
       self.atm_number = atm_number
       self.atm_pin = atm_pin
    def BalanceEnquiry(self):
        print("Your balance is Rs.50000 ")
    def CashWithdrawl(self,amount):
        newAmount = 50000 - amount
        print("Your balance is :",newAmount)
def main():
    atm_number = input("Enter your ATM Number here :")
    atm_pin = input("Enter your ATM Pin here :")
    newUser = Atm(atm_number,atm_pin)
    option = int(input("Choose : 1. Balance Enquiry 2.Cashwithdrawl :"))
    if(option == 1):
        newUser.BalanceEnquiry()
    elif(option == 2):
        amount = int(input("Enter any amount to withdraw :"))
        newUser.CashWithdrawl(amount)
    else:
        print("Enter a valid number")
main()

    