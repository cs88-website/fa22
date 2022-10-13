class BaseAccount:
    """Create named accounts with a balance that is
    - increased by account_deposit
    - decreased by account_withdrawl
    """
    # Constructor
    def __init__(self, name, initial_deposit=0, account_number=0, bank=None):
        # Initialize the instance attributes
        self._name = name
        self._bank = bank
        self._acct_no = account_number
        self._balance = initial_deposit
        self.test_attribute = 'Base Account'

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


class CheckingAccount(BaseAccount):
    def __init__(self, name, initial_deposit, account_number=0, bank=None):
        # Use superclass initializer
        BaseAccount.__init__(self, name, initial_deposit, account_number, bank)
        # Alternatively:
        # super().__init__(name, initial_deposit)
        # Additional initialization
        self._type = "Checking"

    def account_type(self):
        return self._type

    # Just for debugging / example:
    def show_superclass(self):
        return super()

    def print_super(self):
        print(super())

class SavingsAccount(BaseAccount):
    interest_rate = 0.02

    def __init__(self, name, initial_deposit, account_number, bank):
        # Use superclass initializer
        super().__init__(name, initial_deposit, account_number, bank)
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

class Bank:
    def __init__(self, name, initial_account_number=1000):
        self.name = name
        self.__next_account_no = initial_account_number
        self.__accounts = []

    def new_account(self, name, initial_deposit=0, account_type=CheckingAccount):
        account_no = self.__next_account_no
        account = account_type(name, initial_deposit, account_no, self)
        self.__next_account_no += 1
        self.__accounts.append(account)
        return account

    def show_accounts(self):
        for acct in self.__accounts:
            print(acct)

    def all_accounts(self):
        return tuple(self.__accounts)

    def __len__(self):
        return len(self.__accounts)

    def total_assets(self):
        return sum(map(lambda a: a.account_balance(), self.__accounts))

berkeley = Bank('UC Berkeley')

# cs88 = CheckingAccount('CS88', 1000)
