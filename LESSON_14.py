# Create a class Product with properties name, price, and quantity.
# Create a child class Book that inherits from
# Product and adds a property author and a method called read that prints
# information about the book.

class Product(object):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Book(Product):
    def __init__(self, name, price, quantity, property_auth):
        super().__init__(name, price, quantity)
        self.property_auth = property_auth

    def read_book(self):
        print(f"Information about the book: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\nProperty author: {self.property_auth}.")

misto = Book('The book "City', 400, 5, "Demontovich")
misto.read_book()

# 2. Create a class Restaurant with properties name, cuisine, and menu.
# The menu property should be a dictionary with keys being the dish name
# and values being the price. Create a child class FastFood that inherits
# from Restaurant and adds a property drive_thru (a boolean indicating whether
# the restaurant has a drive-thru or not) and a method called order which takes
# in the dish name and quantity and returns the total cost of the order. The method
# should also update the menu dictionary to subtract the ordered quantity from the
# available quantity. If the dish is not available or if the requested quantity is
# greater than the available quantity,
# the method should return a message indicating that the order cannot be fulfilled.

menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, name_dish, quant: int):
        order = 0
        for key in self.menu:
            if name_dish == key:
                dish = self.menu[name_dish]
                if dish['quantity'] >= quant:
                    order = dish['price'] * quant
                    dish['quantity'] -= quant
                    return order
                else:
                    return 'Requested quantity not available'
            else:
                return 'Dish not available'


mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))
print(mc.order('burger', 15))
print(mc.order('soup', 5))

# 3.(Optional) A Bank

# Using the Account class as a base class, write two derived classes called SavingsAccount and CurrentAccount.
# A SavingsAccount object, in addition to the attributes of an Account object, should have an interest attribute
# and a method which adds interest to the account. A CurrentAccount object, in addition to the attributes of an
# Account object, should have an overdraft limit attribute.
# Now create a Bank class, an object of which contains an array of Account objects. Accounts in the array could be
# instances of the Account class, the SavingsAccount class, or the CurrentAccount class. Create some test accounts (some of each type).
# Write an update method in the Bank class. It iterates through each account, updating it in the following ways:
# Savings accounts get interest added (via the method you already wrote); CurrentAccounts get a letter sent if they
# are in overdraft. (use print to 'send' the letter).The Bank class requires methods for opening and closing accounts,
# and for paying a dividend into each account.

class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'
    
class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest
    
    def interest_to_account(self):
        interest_sum = self._balance * self.interest
        self._balance += interest_sum


class CurrentAccount(Account):
    def __init__(self, balance, account_number, limit):
        super().__init__(balance, account_number)
        self.limit = limit
    
    def sending_letter(self):
        if self._balance < self.limit:
            print(f'Account {self._account_number} is in overdraft.')


class Bank:
    def __init__(self, accounts: list[Account]):
        self.accounts = accounts

    def open_account(self, account):
        self.accounts.append(account)
    
    def close_account(self, account):
        self.accounts.remove(account)
    
    def dividend(self, dividend):
        for account in self.accounts:
            account.deposit(dividend)
    
    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.interest_to_account()
            elif isinstance(account, CurrentAccount):
                account.sending_letter()


account_simpl = Account.create_account("UA1348")
savings_acc = SavingsAccount(3000, "UA1234", 0.20)
current_acc = CurrentAccount(4000, "UA1470", -500)

lister = [account_simpl, savings_acc, current_acc]
bank = Bank(lister)

bank.open_account(account_simpl)
bank.open_account(savings_acc)
bank.open_account(current_acc)
bank.dividend(700)
bank.update()

print(account_simpl)
print(savings_acc)
print(current_acc)
