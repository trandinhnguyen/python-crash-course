class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def decribe_user(self):
        print(f'First name: {self.first_name.title()}')
        print(f'Last name: {self.last_name.title()}')

    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}')


me = User('nguyen', 'tran')
you = User('anh', 'nguyen')
he = User('huong', 'vu')

me.decribe_user()
you.greet_user()
he.decribe_user()
