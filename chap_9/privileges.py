from login_attempts import User


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


if __name__ == '__main__':
    me = Admin('nguyen', 'tran')
    me.decribe_user()
    me.privileges.show_privileges()
