class person:
    def __init__(self,name , age, address):
        self.name=name
        self.age=age
        self.address=address
    def Talk(self):
        print(f"hi everybody! this is {self.name} I am {self.age} years old")
    def leave(self):
        print(f'nice to meet you . Goof bye ! --{self.name}-- left')



class Employ(person):
    def __init__(self, Experience, jobtitle, name, age, address):
        super().__init__(name, age, address)
        self.Experience=Experience
        self.jobtitle=jobtitle


s = Employ(4,3,2,1)




