class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def decribe_user(self):
        print(f'First name: {self.first_name.title()}')
        print(f'Last name: {self.last_name.title()}')

    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}')

    def increase_login_attemps(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


if __name__ == '__main__':
    me = User('nguyen', 'tran')

    me.increase_login_attemps()
    me.increase_login_attemps()
    me.increase_login_attemps()

    print(me.login_attempts)

    me.reset_login_attempts()

    print(me.login_attempts)
