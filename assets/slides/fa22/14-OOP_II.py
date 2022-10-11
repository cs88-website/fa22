class Point:
    def __init__(self, x, y):
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

    def __str__(self):
        """Returns a nicely readable format when we call print()"""
        # Remember, this is just shorthand:
        # return "Point (x: " + str(self.x) + ", y: " + str(self.y) + ")"
        return f'Point (x: {self.x}, y: {self.y})'

class BaseAccount:
    """Create named accounts with a balance that is
    - increased by account_deposit
    - decreased by account_withdrawl
    """
    # Class astributes outside and class defs
    _account_number_seed = 1000
    _all_accounts = []

    # Constructor
    def __init__(self, name, initial_deposit):
        # Initialize the instance attributes
        self._name = name
        self._acct_no = BaseAccount._account_number_seed
        BaseAccount._account_number_seed += 1
        self._balance = initial_deposit
        BaseAccount._all_accounts.append(self)

    # Selectors
    def account_name(self):
        return self._name

    def account_balance(self):
        return self._balance

    def account_number(self):
        return self._acct_no

    # Operations
    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        self._balance -= amount
        return self._balance

    def account_type(self):
        return "Base"

    # Display representation
    def __repr__(self):
        return f'<{self.account_type()}Account: {self.account_name()}-{self.account_number()}>'

    # Print representation
    def __str__(self):
        return f'{self.account_type()}Account: {self.account_name()}-{self.account_number()} Balance: {self._balance}'

    def show_accounts():
        for account in BaseAccount._all_accounts:
            print(account)

class CheckingAccount(BaseAccount):
    def __init__(self, name, initial_deposit):
        # Use superclass initializer
        BaseAccount.__init__(self, name, initial_deposit)
        # Alternatively:
        # super().__init__(name, initial_deposit)
        # Additional initialization
        self._type = "Checking"

    def account_type(self):
        return self._type

    # Just for debugging / example:
    def show_superclass(self):
        return super()

class SavingsAccount(BaseAccount):
    interest_rate = 0.02

    def __init__(self, name, initial_deposit):
        # Use superclass initializer
        super().__init__(name, initial_deposit)
        # BaseAccount.__init__(self, name, initial_deposit)
        # Additional initialization
        self._type = "Savings"

    def account_type(self):
        return self._type

    def accrue_interest(self):
        self._balance = self._balance * (1 + SavingsAccount.interest_rate)

    # Display representation
    def __repr__(self):
        return f'<{self.account_type()}Account: {self.account_name()}-{self.account_number()} @ {SavingsAccount.interest_rate * 100}%>'

    # Print representation
    def __str__(self):
        return self.__repr__()


cs88 = CheckingAccount('CS88', 1000)
