class Dog():
    """ 1 """
    def __init__(self,name,age):
        """chushihua"""
        self.name = name
        self.age = age
    
    def sit(self):
        """monizuo"""
        print(self.name.title() + " is sitting. ")
    
    def dun(self):
        """monidun"""
        print(self.name.title() + " is dunzhe. ")

my_dog = Dog('hello',10)
print(my_dog.name.upper())
print(str(my_dog.age))
my_dog.dun()
my_dog.sit()


