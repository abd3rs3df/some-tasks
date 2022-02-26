class User:
    def __init__(self,fristName,lastName,gender,age ,address):
        self.fristName =fristName
        self.lastName=lastName
        self.gender=gender
        self.age=age
        self.address=address
        self.login_attempts=0


    def describe_user(self):
        print(f''' 
fris name : {self.fristName} 
last name : {self.lastName}
gender    : {self.gender}
age       : {self.age}
address  :  {self.address}''')

    def greet_user(self):
        print(f"welcome {self.fristName+' '+self.lastName}")

    def increment_login_attempts(self):
        self.login_attempts+=1

    def rest_login_attempts(self):
        self.login_attempts=0


class Admin(User):
    privileges = ['can add post ', 'can delete post', 'can ban user']
    def __init__(self, fristName, lastName, gender, age, address):
        super().__init__(fristName, lastName, gender, age, address)

    def show_privileges(self):
        for priv in  self.privileges:
            print(priv)



user=User('abdullah','fawaz','male',19,'mousl')
user.describe_user()
user.greet_user()


user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)

user.rest_login_attempts()
print(user.login_attempts)

admin=Admin('abdullah','fawaz','male',19,'mousl')
admin.show_privileges()

