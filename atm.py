class ATM:
    def __init__(self):
        self.balance = 10000
        self.five_hundred = 0
        self.two_hundred = 0
        self.fifty = 0
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
            return

        while amount >= 500:
            self.balance -= 500
            self.five_hundred += 1
            amount -= 500

        while amount >= 200:
            self.balance -= 200
            self.two_hundred += 1
            amount -= 200

        while amount >= 50:
            self.balance -= 50
            self.fifty += 1
            amount -= 50

    def display_notes(self):
        print("500 notes:", self.five_hundred)
        print("200 notes:", self.two_hundred)
        print("50 notes:", self.fifty)
        print("Remaining balance:", self.balance)

def main():
    atm = ATM()
    amount = int(input("Enter amount: "))
    atm.withdraw(amount)
    atm.display_notes()

main()

