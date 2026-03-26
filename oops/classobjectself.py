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
"""class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks 
    def is_pass(self):
        return self.marks>40
st1=student("pavan",85)
st2=student("kumar",35)
st3=student("yarramsetty",99)
print(st1.is_pass())    
print(st2.is_pass())
print(st3.is_pass())"""
#area of rectangle,circle,square
"""class rectangle:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def area(self):
        print(self.length*self.breath)
rc1=rectangle(5,10)
rc1.area()
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area_circumference(self):
        print(f"area: {self.radius*self.radius*3.14}")
        print(f"circumference: {2*3.14*self.radius}")
c1=circle(5)
c1.area_circumference()
class square():
    def __init__(self,side):
        self.side=side
    def area(self):
        print(self.side*self.side)
s1=square(5)
s1.area()"""
#employee salary system 
"""class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def yearly_salary(self):
        print(f"yearly salary of {self.name} is {self.__salary*12}")
emp1=employee("pavan",100000)
emp1.yearly_salary()"""
#library book system if avalible true else false
"""class book:
    def __init__(self,title,author,is_available=True):
        self.title=title
        self.author=author
        self.is_available=is_available
    def borrow_book(self):
        if self.is_available:
            self.is_available=False
            print(f"you have borrowed {self.title} by {self.author}")
        else:
            print(f"sorry {self.title} is not available right now")
    def return_book(self):
        self.is_available=True
        print(f"you have returned {self.title} by {self.author}")
book1=book("atomic habits","pavan")
book2=book("the silent patient","kumar")
book1.borrow_book()
book2.borrow_book()
book1.return_book()"""
#student managment system
"""class student:
    def __init__(self,name,marks=[]):
        self.name=name
        self.marks=marks
    def average(self):
        self.average=sum(self.marks)//len(self.marks)
    def grade(self):
        self.average()
        avg=self.average
        if avg>=90:
            return "A"
        elif avg>=80:
            return "B"
        elif avg>=70:
            return "C"
        elif avg>=60:
            return "D"
        else:
            return "F"
st1=student("pavan",[85,90,95])
print(st1.grade())    """ 
"""class AreaCalculator:
    def __init__(self, radius, height, length, breadth):
        self.radius = radius
        self.height = height
        self.length = length
        self.breadth = breadth
    def rectangle_area(self):
        return self.length * self.breadth
    
    def square_area(self):
        return self.length * self.length
    
    def circle_area(self):
        return 3.14 * self.radius * self.radius

    def cylinder_area(self):
        return 2 * 3.14* self.radius * (self.radius + self.height)

    def hemisphere_area(self):
        return 2 * 3.14* self.radius * self.radius

    def sphere_area(self):
        return 4 * 3.14* self.radius * self.radius

    def main_menu(self):
        while True:
            print("1. Rectangle")
            print("2. Square")
            print("3. Circle")
            print("4. Cylinder")
            print("5. Hemisphere")
            print("6. Sphere")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.length = float(input("Enter length: "))
                self.breadth = float(input("Enter breadth: "))
                print("Area of Rectangle =", self.rectangle_area())

            elif choice == 2:
                self.length = float(input("Enter side length: "))
                print("Area of Square =", self.square_area())

            elif choice == 3:
                self.radius = float(input("Enter radius: "))
                print("Area of Circle =", self.circle_area())

            elif choice == 4:
                self.radius = float(input("Enter radius: "))
                self.height = float(input("Enter height: "))
                print("Surface Area of Cylinder =", self.cylinder_area())

            elif choice == 5:
                self.radius = float(input("Enter radius: "))
                print("Surface Area of Hemisphere =", self.hemisphere_area())

            elif choice == 6:
                self.radius = float(input("Enter radius: "))
                print("Surface Area of Sphere =", self.sphere_area())
                break

            else:
                print("Invalid choice! Please try again.")
calculator = AreaCalculator(0, 0, 0, 0)  
calculator.main_menu() """ 
#oops question 2
"""class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print(f"name:{self.name}, rollno:{self.rollno}, marks:{self.marks}")
st1=student("pavan",7,85)
st2=student("kumar",17,35)    
st1.display()
st2.display()"""