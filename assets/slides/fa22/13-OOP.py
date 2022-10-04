class Test:
    def __init__(self, value):
        self.__value = value

    def show_value(self):
        return self.__value

class Point:
    def __init__(self, x, y):
        print('Point: ', self)
        self.x = x
        self.y = y

    def subtract(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __sub__(self, other):
        """Allows us to write point3 = point1 - point2"""
        return self.subtract(other)

    def distance(self, other):
        diff = self - other
        return (diff.x ** 2 + diff.y ** 2) ** 0.5

class BaseAccount:
    def __init__(self, name, initial_deposit=0):
        self._name = name
        self._balance = initial_deposit

    def balance(self):
        return self._balance

    def withdraw(self, amount):
        self._balance -= amount
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    @property
    def name(self):
        return self._name

# Make a new account
my_account = BaseAccount('CS88', 100)
# Access Data
my_account._balance
my_account.balance()
# notice how we we calling the class itself.
# my_account is the self in the balance method.
BaseAccount.balance(my_account)

cs88 = BaseAccount('CS88', 100)
data8 = BaseAccount('DATA8', 100)

data8.withdraw(25)

#data8.balance()
cs88.balance()

class BaseAccount2:
    account_number_seed = 1000
    accounts_list = []

    def __init__(self, name, initial_deposit=0):
        self._name = name
        self._balance = initial_deposit
        self._acct_no = BaseAccount2.account_number_seed
        BaseAccount2.account_number_seed += 1
        BaseAccount2.accounts_list += [self]

    def name(self):
        return self._name

    def balance(self):
        return self._balance

    def withdraw(self, amount):
        self._balance -= amount
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def account_no(self):
        return self._acct_no

    # Can optionally use @classmethod
    def accounts():
        return BaseAccount2.accounts_list

    def show_accounts():
        for account in BaseAccount2.accounts():
            print(account.name(),
                  account.account_no(),account.balance())


data100 = BaseAccount2('DATA100')
cs61b = BaseAccount2('CS61B')

# print(data100.account_no())

# print(cs61b.account_no())

BaseAccount2.account_number_seed
# print(BaseAccount2.show_accounts())
