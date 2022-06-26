from abc import ABC, abstractmethod
from distutils.command.build_scripts import first_line_re

#abstract class
class Person(ABC):
    first='first_name'
    last='last'
    @abstractmethod
    def fullname(self):
        pass

class Employee(Person):
    
    raise_amount=1.04
    num_of_emps=0

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@email.com'
    
    #with this you can do empinstance.fullname without the brackets
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    #with this you can do:
    # empinstance.fullname='yongwook kim'
    @fullname.setter
    def fullname(self, name):
        first, last=name.split(' ')
        self.first=first
        self.last=last
    
    @fullname.deleter
    def fullname(self):
        print('delete name')
        self.first=None
        self.last=None

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
    
    #special methods    
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay+other.pay

#inheritance
class Developer(Employee):
    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        #Employee.__init__(first, last, pay)
        #is also possible, should be used in multiple inheritance
        self.language=language

emp1=Employee('yongwook', 'kim', 50000)
emp2=Employee('seeun', 'kim', 60000)
#print(str(emp1))
print(repr(emp1))
print(emp1+emp2)
print(emp1.fullname)