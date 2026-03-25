'''class animal:
    def speak(self):
        print("woof")
class dog(animal):   
    def food(self):
        print("eats bones")
puppy=dog()
puppy.speak()
puppy.food()'''
#vehicle
'''class vehical:
    def brand(self,company):
        self.company=company
        print(f"car is from {self.company}")
class car(vehical):
    def model(self,model):
        self.model=model
        print(f"car model is {self.model}")
car1=car() 
car1.brand("toyota")
car1.model("corolla")'''
#shape and area
'''class shape:
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
c=circle(5)
print("area of circle is", c.area()) '''       
#employee and manager
'''from os import name
class employee:
    def __init__(self.name):
        self.name=name
    def show_details(self):
        print(f"employee name:{self.name}")
class manager(employee):
    def __init__(self,name,dep):
        super().__init__(name)
        self.dep=dep
    def assign_task(self,task):
        print(f"manager {self.name} assigned task: {task} in department {self.dep}")
emp=employee("pavan")
emp.show_details()  
mgr=manager("kumar","IT")
mgr.show_details()  
mgr.assign_task("complete project")'''
#multilevel inheritance
'''class device:
    def can_call(self,call):
        self.call=call
        print("this can call")
class phone(device):
    def sport(self,game):
        self.game=game
        print("this can play games")
class smartphone(phone):
    def all_in_one(self,vdos):
        self.vdos=vdos 
        print("preform all tasks")               
mobile=smartphone()
mobile.sport("cricket")
mobile.can_call("yes")
mobile.all_in_one("video calling")'''