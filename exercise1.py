import datetime
from typing import Dict


class Account:
    # this will increment every new instance
    next_number_of_account = 111111111

    # constructor of Account class
    def __init__(self, name, balance, credit_line=1500):
        self.name = name
        self.balance = balance
        self.credit_line = credit_line
        self.account_number = self.account_number_generator()

    # generator for account numbers
    def account_number_generator(self):
        # increment to the next account number
        Account.next_number_of_account += 1
        # disconnect class variable next_number_of_account from the class
        self.next_number_of_account += 0 
        return self.next_number_of_account

    # get the balance
    def get_balance(self):
        return self.balance
     
    # private decorators for this class only
    ########################################################################
    class _Decorators:
        # check validity of the action
        @classmethod
        def safe_actions(cls, func):
            def safe_func(*args, **kwargs):
                if 'amount' in kwargs and kwargs.get('amount') <= 0:
                    print("amount should be a positive number, not ", kwargs.get('amount'))
                    return False
                if args[1] <= 0:
                    print("amount should be a positive number, not ", args[1])
                    return False
                return func(*args, **kwargs)
            return safe_func

        # print the time of the action
        @classmethod
        def action_time(cls, func):
            def timed_func(*args, **kwargs):
                print(datetime.datetime.now())
                return func(*args, **kwargs)
            return timed_func
    ########################################################################

    # withdraw function
    @_Decorators.action_time
    @_Decorators.safe_actions
    def withdraw(self, amount):
        if self.get_balance() - amount < (0 - self.credit_line):
            print("withrawal for account ", self.account_number, " of ", amount, " ILS")
            print("not enough credit line for withdrawal.\ntried to withdraw amount of ",
                  amount, " but the balance is ", self.get_balance(),
                  " and the credit line is ", self.credit_line)
            return False
        self.balance -= amount
        print("successful withdrawal")
        return True

    # deposit function
    @_Decorators.action_time
    @_Decorators.safe_actions
    def deposit(self, amount):
        print("deposit for account ", self.account_number, " of ", amount, " ILS")
        self.balance += amount
        print("successful deposit")

    # transfer function
    @_Decorators.action_time
    @_Decorators.safe_actions
    def transfer(self, amount, another_account):
        if self.account_number == another_account.account_number:
            print("can not transfer money from an account to itself (account number ",
                  self.account_number, ")")
            return False
        print("transfer from account ", self.account_number, " to account ",
              another_account.account_number, " of ", amount, " ILS")
        succeeded = self.withdraw(amount)
        if not succeeded:
            return False

        another_account.deposit(amount)
        print("successful transfer")
        return True


# generator for account balance
def generator_for_account_balance(accounts_dictionary):
    for account in accounts_dictionary.values():
        yield "account number: " + str(account.account_number) + ", has balance of " + \
              str(account.get_balance()) + " ILS"


# create the accounts
a = Account("shalom shlomomo", 99999)
b = Account("avichai avisror", 88888)
c = Account("naomi nechemia", 77777)
d = Account("moshe ovadia", 66666)

# create the dictionary and put all the accounts
dictionary_of_accounts: Dict[int, Account] = {a.account_number: a, b.account_number: b,
                                              c.account_number: c, d.account_number: d}
