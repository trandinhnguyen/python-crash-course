from login_attempts import User


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


if __name__ == '__main__':
    me = Admin('nguyen', 'tran')
    me.show_privileges()
