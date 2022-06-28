import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.withdrawl = 0

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.withdrawl += amount
            return True
        else:
            return False

    def get_balance(self):
        bal = 0
        for i in self.ledger:
            bal += i['amount']
        return bal

    def transfer(self, amount, categ):

        if self.check_funds(amount):
            des1 = 'Transfer to ' + categ.name
            des2 = 'Transfer from ' + self.name
            self.ledger.append({'amount': -amount, 'description': des1})
            categ.deposit(amount, des2)
            return True
        else:
            return False

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount <= balance:
            return True
        else:
            return False

    def __repr__(self):
        l = (30 - len(self.name)) // 2
        title = '*' * l + self.name + '*' * l
        string = ''
        for i in self.ledger:
            string += i['description'][:23].ljust(23) + str('{:.2f}'.format(
                i['amount'])).rjust(7) + '\n'
            totalstr = 'Total: ' + str(self.get_balance())
        return title + '\n' + string + totalstr


def create_spend_chart(c):
    title = 'Percentage spent by category'
    bar = ''
    categ = '\n    '
    sum = 0
    for i in c:
        sum += i.withdrawl
    percent = [math.ceil(((i.withdrawl * 100) / sum)) for i in c]

    for i in range(100, -10, -10):
        bar += '\n' + str(i).rjust(3) + '| '
        for p in percent:
            if p >= i:
                bar += 'o  '
            else:
                bar += '   '

    l = len(c)
    max = 0
    for i in c:
        if max < len(i.name):
            max = len(i.name)
    categ += '-' * ((len(c) * 3) + 1)
    for i in range(max):
        categ += '\n' + ' ' * 5
        for j in c:
            try:
                categ += j.name[i] + '  '
            except:
                categ += '   '

    return title + bar + categ
