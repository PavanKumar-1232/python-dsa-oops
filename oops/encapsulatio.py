#############################################################################encapsulation 
'''class student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    def get_name(self):
        return self.__name
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if marks>=0:
            self.__marks=marks
        else:
            print("marks cannot be negative")
st=student("pavan",85)  
st.set_marks(90)
print(st.get_name())
print(st.get_marks())   '''
'''class box:
    def __init__(self,weight):
        self._weight=weight
    def get_weight(selg):
        return self._weight
    def set_weight(self,weight):
        if weight>0:
            self._weight=weight
        else:
            print("weight cannot be negative")
b=box(10)   
b.set_weight(20)
print(b.get_weight())  '''
#bank and its encapsulation
'''class bankaccount:
    def __init__(self,balance,pin):
        self.__balance=balance
        self.__pin=pin
    def check_balance(self,pin):
        if pin==self.__pin:
            print({self.balance})
        else:
            print("incorrect pin")
    def withdraw(self,amount,pin):
        if pin!=self.__pin:
            print("incorrect pin withdraw denied!")
        elif amount<0:
            print("valid amount")
        elif amount>self.__balance:
            print("insuffient funds")
        else:
            self.__balance -=amount    
            print(self.__balance)
acc=bankaccount(132231,"1432")
acc.check_balance(1111)
acc.check_balance(1432)          
acc.withdraw(1000,"1432")
acc.withdraw(1000,"1111")   '''
#product and discount
'''class product:
    def __init__(self,price):
        self.__price=price
    def discount(self):
        return self.__price*0.7
car=product(1000000)
print(car.discount())'''
#user and password
'''class user:
    def __init__(self,username,password):
        self.__username=username
        self.__password=password
    def check_username(self):
        return self.__username
    def check_password(self,old_password, new_password):
        if old_password==self.__password:
            if len(new_password)>=6:
                self.__password=new_password
                print("password updated sucessfully")
            else:
                print("enter long password")
        else:
            print("incorrect old password")            
def verify_login(self,password):
    if password==self.__password:
        print("login sucessfull")   
    else:
        print("login failed")
user1=user("pavan","123456")
user1.verify_login("123456")
user1.check_password("123456","654321") 
user1.verify_login("654321")
print(user1.check_username())   '''