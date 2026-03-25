###############################################################################abstract class
'''from abc import ABC,abstractmethod
class animal:
    @abstractmethod
    def make_sound(self):
        pass
class dog(animal):
    def make_sound(self):
        print("woof")
class cat(animal):
    def make_sound(self):
        print("meow")
Dog=dog()
Cat=cat()
Dog.make_sound()
Cat.make_sound() '''    
#
'''from abc import ABC,abstractmethod
class shape:
    @abstractmethod
    def area(self):
        pass
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
sq=square(5)
print(sq.area())  '''       
#turn on and turn off
'''from abc import ABC, abstractmethod
class device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
class tv(device):
    def turn_on(self):
        print("TV is now ON")

    def turn_off(self):
        print("TV is now OFF")
TV=tv()
TV.turn_on()
TV.turn_off()'''
#employee
'''from abc import ABC,abstractmethod
class employee:
    @abstractmethod
    def calculate_salary(self):
        pass
class fulltimeemployee(employee):
    def __init__(self,base_salary):
        self.base_salary=base_salary
    def calculate_salary(self):
        return self.base_salary
class parttimeemployee(employee):
    def __init__(self,hourly_rate,hours_worked):
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
    def calculate_salary(self):
        return self.hourly_rate*self.hours_worked   
emp1=fulltimeemployee(50000)
emp2=parttimeemployee(20,100)   
print(emp1.calculate_salary())
print(emp2.calculate_salary())'''
#bank
'''from abc import ABC, abstractmethod
class account:
    @abstractmethod
    def withdraw(self,amount):
        pass
class savingaccount(account):
    def __init__(self,balance):
        self.balance=balance
        if self.balance<1000:
            print("minimum balance should be 1000")
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient funds")
        else:
            self.balance-=amount
            print(f"withdrawn {amount}, remaining balance is {self.balance}")               
class currentaccount(account):  
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient funds")
        else:
            self.balance-=amount
            print(f"withdrawn {amount}, remaining balance is {self.balance}")       
s1=savingaccount(5000)
s1.withdraw(2000) '''