from datetime import datetime

class Amount:
    def __init__ (self,amount,timestamp,transaction_type):
        self.__amount = float(amount)
        self.__timestamp = timestamp
        self.__transaction_type = transaction_type
    def __str__(self):
        return f'Amount: {self.__amount}, Transaction Type: {self.__transaction_type}, Timestamp: {self.__timestamp}'

class PersonalAccount:
    def __init__(self,name,account_number):
        self.__name = name
        self.__account_number = account_number
        self.__balance = 0.0
        self.__transactions = []
    def deposit(self,amount):
        self.__balance += amount
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = Amount(amount, timestamp, "Deposit")
        self.__transactions.append(transaction)
    def withdraw(self,amount):
        if amount > self.__balance:
            print('Transaction failed: Not enough balance')
        else:
            self.__balance -= amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction = Amount(amount, timestamp, "Withdrawal")
            self.__transactions.append(transaction)
    def print_history(self):
        for transaction in self.__transactions:
            print(transaction)
    def get_balance(self):
        print(self.__balance)

if __name__ == "__main__":
    acc=PersonalAccount(input('Enter your name: '), input('Enter your account number: '))
    acc.deposit(int(input('Enter deposit amount: ')))
    acc.withdraw(int(input('Enter withdrawal amount: ')))
    acc.print_history()
    acc.get_balance()