class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello"+self.name)
s1=student("Mohit",24)
s2=student("Manu",25)
print(s1.name)
print(s1.age)


######del s1    #main


print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)