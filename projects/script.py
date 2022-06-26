class Class1:
    def m(self):
        print("class1")

class Class2(Class1):
    def m(self):
        print("class2")

class Class3(Class1):
    def m(self):
        print("class3")

class Class4(Class3, Class2):
    pass


obj=Class4()
obj.m()