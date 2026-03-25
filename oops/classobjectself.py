#########################################################oops#######################################################
#class and object
'''class laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display_info(self):
        print(f"{self.brand}")
        print(f"{self.price}") 
             
lappy=laptop("hp",700000)              
lappy.display_info() '''
#reactangle area
'''class reactangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
r1=reactangle(4,5)
print(r1.area())'''   
#book with title and author
'''class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
book1=book("atomic habits","pavan")        
print(book1.author)
print(book1.title)  '''          
#pen and methods
'''class pen:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def write(self):
        print(f"writing in {self.color} {self.brand} pen")
pen1=pen("ox","blue")
pen2=pen("elkos","black")   
pen1.write() '''
#student and name
'''class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno  
st1=student("pavan",7)
st2=student("kumar",17)
print(st1.name, st1.rollno)
print(st2.name, st2.rollno)'''
#employee with namen and salary
'''class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"name:{self.name},salary :{self.salary}")
emp1=employee("pavan",10000000000000000)        
emp2=employee("kumar",2000000000000000)
emp1.display()'''
#mobile and discount
'''class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def discount(self):
        self.price=self.price*0.9
        print(self.price)
mobile1=mobile("iphone",100000)
mobile2=mobile("samsung",99999)
mobile1.discount()
mobile2.discount()'''
#movie classic
'''class movie:
    def __init__(self,title,year):
        self.title=title
        self.year=year
    def is_classic(self):
        if self.year<2000:
            print("true") 
        else:
            print("no its not a classic")
m1=movie("mayabazar",1970)
m1.is_classic()'''
#point with x,y
'''class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
    def display(self):
        print(f"point({self.x},{self.y})")    
p=point(2,3)
p.display()
p.move(-5,3)
p.display()'''
#bank 
'''class bankaccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient blance")
        else:
            self.balance -=amount
    def display_balance(self):
        print(self.balance)                   
acc=bankaccount()
acc.display_balance()
acc.deposit(5000)
acc.withdraw(2000)
acc.display_balance()  '''