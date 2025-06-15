# # Inheritance------------------------------------------------------>

######################## single
class GrandFather:
    def __init__(self, color, first_name):
        self.color= color
        self.first_name=first_name
        
class Father(GrandFather):
    def __init__(self, hobby, color,first_name):
        super().__init__(color,first_name)
        self.hobby=hobby
        
gf1= GrandFather('red','chowdhury')
f1= Father('cricket','red','chowdhury')
print(f1.color)

######################## multiple
class GrandFather:
    def __init__(self, color, first_name):
        self.color= color
        self.first_name=first_name
    def gf_method(self):
        print("i am from grandfather")
        
class Father(GrandFather):
    def __init__(self, hobby, color,first_name):
        super().__init__(color,first_name)
        self.hobby=hobby
    def f_method(self):
        print("i am from father")
        
class Children(Father, GrandFather):
    def __init__(self, fashion, hobby, color, first_name):
        super().__init__(hobby, color, first_name)
        self.fashion= fashion
        
c1= Children("test", "football", "blue", "dev")
c1.gf_method()
c1.f_method()
print(c1.fashion, c1.color, c1.first_name)
___________________________________________________________
class GrandFather:
    def __init__(self, color, first_name):
        self.color= color
        self.first_name=first_name
    def gf_method(self):
        print("i am from grandfather")
        
class Father(GrandFather):
    def __init__(self, hobby):
        self.hobby=hobby
    def f_method(self):
        print("i am from father")
        
class Children(Father, GrandFather):
    def __init__(self, fashion, hobby, color, first_name):
        Father.__init__(self, hobby)
        GrandFather.__init__(self, color, first_name)
        self.fashion= fashion
          
c1= Children("test", "football", "blue", "dev")
c1.gf_method()
c1.f_method()
print(c1.fashion, c1.color, c1.first_name)

####################### multilevel
class GrandFather:
    def __init__(self, color, first_name):
        self.color= color
        self.first_name=first_name
    def gf_method(self):
        print("i am from grandfather")
        
class Father(GrandFather):
    def __init__(self, hobby, color, first_name):
        super().__init__( color, first_name)
        self.hobby=hobby
    def f_method(self):
        print("i am from father")
        
class Children(Father, GrandFather):
    def __init__(self, fashion, hobby, color, first_name):
        super().__init__( hobby, color, first_name)### this is main cause multilevel
        self.fashion= fashion
          
c1= Children("test", "football", "blue", "dev")
c1.gf_method()
c1.f_method()
print(c1.fashion, c1.color, c1.first_name)
        
#################### hierarchical
## same clsss jodi multple class ke inherit kore setake hieararchical bole
class Vehical:
    def engine_type(self):
        print("Vehical has an engine")
        
class Car(Vehical):
    def num_door(self):
        print("car has 4 doors")
        
class Truck(Vehical):
    def load_capacity(self):
        print("Truck can carry tons") 
        
car = Car()
car.engine_type()
car.num_door()
truck = Truck()
truck.engine_type()
truck.load_capacity()
#################### hybrid
class Shape:
    def area(self):
        print("Calculating area...")

class Polygon(Shape):
    def sides(self):
        print("Polygon has multiple sides")

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length= length
        self.breadth= breadth
        
    def area(self):
        return self.length*self.breadth
    
rec= Rectangle(10,5)
print(rec.area())
rec.sides()
rec.area()

    

class Vehicle:#parents class
    def __init__(self,model,year,wheels):
        self.model=model
        self.year=year
        self.wheels=wheels
    def details(self):
        print(f"{self.model} are register {self.year} year and has {self.wheels} wheels")
        
class Car(Vehicle):#child class
    def __init__(self,model, year, wheels,doors):
        super().__init__(model, year, wheels)#super are built in function that pass parent classa attributes
        self.doors=doors
    
class Bike(Vehicle):#child class
    def __init__(self, model, year, wheels,c_angle):
        super().__init__(model, year, wheels)
        self.c_angle=c_angle
        
tata=Vehicle("abc",2015,5)
tata.details()

bmw=Car("y20",2025,4,5)
bmw.details()
print(f"y20 has {bmw.doors} doors")

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print(f"{self.name} the {self.species} make sound")

class dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="dog")
        self.breed=breed
    def show_breed(self):
        print(f"{self.name} is a {self.breed} dog")

class cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="cat")
        self.color=color
    def show_color(self):
        print(f"{self.name} is a {self.color} cat")
        
animal=Animal("leo","lion")
dogy=dog("tom","deshi")
kity=cat("jerry","brown")

animal.make_sound()
dogy.make_sound()
dogy.show_breed()
kity.make_sound()
kity.show_color()


# # polymorphism------------------------------------------->
####    same function 2 ta class ei ache but akta ekrokom kaj kore
## poly--> Multiple
## morphism --> form

# 1. Methoad Overriding
class GrandFather:
    def greet(self):
        print("Grandfather says")
        
class Father(GrandFather):
    def greet(self):
        print("father says")
        
class Children(Father):
    def greet(self):
        print("Children says")

gf = GrandFather()
f= Father()
c= Children()
gf.greet()
f.greet()
c.greet()

# 2. Methoad Overloading

# class shape:
#     def area(self):# all class has same modeul/function so thats polymorphism
#         pass

# class circle(shape):
#     def __init__(self,redius):
#         self.redius=redius
#     def area(self):
#         return 3.14 * self.redius ** 2
# class square(shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side**2
    
# c=circle(5)
# print(c.area())

# s=square(5)
# print(s.area())


# class Player: #abastrac class
#     def play(self):
#         pass
# class Footballplayer(Player):
#     def __init__(self,club,country):
#         self.club=club
#         self.country=country
#     def play(self):
#         print(f"i love {self.club} club and country {self.country}")
        
        
# class Cricketplayer(Player):
#     def __init__(self,studium):
#         self.studium=studium
#     def play(self):
#         print(f"i love {self.studium} stadium")
        

# a=Footballplayer("PSG","France")
# a.play()
# b=Cricketplayer("Sagorika")
# b.play()

#Encapsulation-----------(public,private)-------------------------------------->
# class Account:
#     def __init__(self,balance):
#         self.__balance=balance #private ( __att )
    
#     def get_balance(self):
#         return self.__balance
    
# a=Account(5)
# print(a.get_balance())


# class Account:
#     def __init__(self,balance):
#         self.__balance=balance #private ( __att )
    
#     def get_balance(self):
#         return self.__balance
    
#     def change_balance(self,val):
#         self.__balance=val
        
#     def flot_bal(self,ff):
#         self.__balance=ff
        
    
# a=Account(5)
# print(a.get_balance())

# a.change_balance(200)
# print(a.get_balance())

# a.flot_bal(6.5)
# print(a.get_balance())

#Abstraction---------------------------------------------------->
#A decorator is a function in Python that allows you\
    # to modify or extend the behavior of another function or method\
        # without altering its actual code.

# from abc import ABC,abstractmethod

# class shape(ABC):
#     @abstractmethod #decorator
#     def area(self):
#         pass
    
# class circle(shape):
#     def area(self):# shape class ee area abstract tai,inherit all shape must need area.
#         return "calculating circle area"
    
# a=circle()
# print(a.area())

# @abstractmethod mane ai method ta sob base class e implement korte hobe must---------------->
#je class gula oi Shape class ke inherit korbe oi class gula te ai area method likhtei hobe

# from abc import ABC,abstractmethod
# class shape(ABC):
#     @abstractmethod #decorator
#     def area(self):
#         pass
    
# class circle(shape):
#     def area(self,r):
#         return (3.1416 * r)
    
# class rectangle(shape):
#     def area(self,a,b):
#         return (a*b)
    
# a=circle()
# print(a.area(5))

# b=rectangle()
# print(b.area(5,4))

# Single Responsibility Principle (SRP).--------------------------->
# # oop part-1 12number slid task 3 
class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print(f"{self.model} is being driven.")


class FuelEfficiencyCalculator:
    def calculate_fuel_efficiency(self, miles, fuel):
        if fuel == 0:
            return 0  # Avoid division by zero
        return miles / fuel


# Example usage
car = Car("Toyota")
car.drive()

fuel_calculator = FuelEfficiencyCalculator()
efficiency = fuel_calculator.calculate_fuel_efficiency(100, 5)
print(f"Fuel Efficiency: {efficiency} miles per gallon")
# Single Responsibility Principle (SRP)--------------------->

# from abc import ABC,abstractmethod

# class shape(ABC):
#     @abstractmethod #decorator
#     def area(self):
#         raise NotImplementedError(" subclassess must implement this method..")
    
# class circle(shape):
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return 3.14 * self.r *self.r
    
# class rectangle(shape):
#     def __init__(self,w,h):
#         self.w=w
#         self.h=h
#     def area(self):
#         return (self.w*self.h)
    
# class square(shape):
#     def __init__(self,a):
#         self.a=a
#     def area(self):
#         return (self.a**self.a)
    
# a=circle(5)
# print(a.area())
# b=rectangle(5,5)
# print(b.area())
# c=square(3)
# print(c.area())

# Open/Closed Principle (OCP)------------------------------------------>

# from abc import ABC, abstractmethod

# # Abstract class for shapes
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def area(self):
#         return self.width * self.height

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
    
#     def area(self):
#         return 0.5 * self.base * self.height

# c= Circle(2)
# print(c.area())

# # Liskov Substitution Principle (LSP)-------------------------------------------------->
# class bird:
#      pass
          
# class flyingbird(bird):#<---inherit bird
#      def fly(self):
#           print("flying")
          
# class sparrow(flyingbird):#<---inherit flyingbird
#      pass

# class penguin(bird):#<---inherit bird
#          pass
    
# sp=sparrow()
# sp.fly()

# class Bird:
#     def move(self):
#         pass

# class FlyingBird(Bird):
#     def move(self):
#         return "Flying"

# class Sparrow(FlyingBird):
#     pass

# class Ostrich(Bird):
#     def move(self):
#         return "Running"

# def make_bird_move(bird: Bird):
#     return bird.move()

# sparrow = Sparrow()
# print(make_bird_move(sparrow))  # Output: Flying

# ostrich = Ostrich()
# print(make_bird_move(ostrich))   # Output: Running

# ostrich = Ostrich()
# print(ostrich.move())   # Output: Running


# # Interface Segregation Principle (ISP)----------------------------------------------->
# class vehicle:
#      pass

# class Derivable(vehicle):
#      def drive(Self):
#           pass
     
# class Flyable(vehicle):
#      def fly(self):
#           pass

# class car(Derivable):
#      def drive(Self):
#           print("driving on road")
     
# class Airplan(Flyable):
#      def fly(Self):
#           print("flying in the sky")
     
# from abc import ABC, abstractmethod
# # Segregated interfaces
# class Workable(ABC):
#     @abstractmethod
#     def work(self):
#         pass

# class Eatable(ABC):
#     @abstractmethod
#     def eat(self):
#         pass

# # Employee class implementing both interfaces
# class Employee(Workable, Eatable):
#     def work(self):
#         return "Working"

#     def eat(self):
#         return "Eating"

# # Robot class only implementing the Workable interface
# class Robot(Workable):
#     def work(self):
#         return "Working"

# # Using the classes
# employee = Employee()
# print(employee.work())  # Output: Working
# print(employee.eat())   # Output: Eating

# robot = Robot()
# print(robot.work())     # Output: Working
# # robot.eat() would raise an error since Robot does not implement the Eatable interface


# # Dependency Inversion Principle (DIP)------------------------------->
# class notificationservice:
#      def send(self,msg):
#           pass
 
# class Emailservice:
#      def send(self,msg):
#           print(f"sending email: {msg}")

# class notification:
#      def __init__(self,service:notificationservice):
#           self.service=service
#      def notify(self,msg):
#           self.service.send(msg)
          
# email_service=Emailservice()

# notification=notification(email_service)
# notification.notify("hello")


# class LightBulb:
#     def turn_on(self):
#         print("LightBulb turned on")

#     def turn_off(self):
#         print("LightBulb turned off")

# class Switch:
#     def __init__(self, bulb: LightBulb):
#         self.bulb = bulb

#     def operate(self):
#         self.bulb.turn_on()

# # Usage
# bulb = LightBulb()
# switch = Switch(bulb)
# switch.operate()  # Output: LightBulb turned on


# from abc import ABC, abstractmethod
# # Abstraction
# class Light(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass

#     @abstractmethod
#     def turn_off(self):
#         pass
# # Concrete implementation of Light
# class LightBulb(Light):
#     def turn_on(self):
#         print("LightBulb turned on")

#     def turn_off(self):
#         print("LightBulb turned off")
# # Another concrete implementation of Light
# class LED(Light):
#     def turn_on(self):
#         print("LED turned on")

#     def turn_off(self):
#         print("LED turned off")
# # High-level module depending on the abstraction
# class Switch:
#     def __init__(self, light: Light):
#         self.light = light

#     def operate(self):
#         self.light.turn_on()
# # Usage
# bulb = LightBulb()
# led = LED()

# switch1 = Switch(bulb)
# switch1.operate()  # Output: LightBulb turned on

# switch2 = Switch(led)
# switch2.operate()  # Output: LED turned on


# Error handling--------------------------------------------------------->

# try:
#     n=int(input())
#     print(10/n)

# except ZeroDivisionError:
#     print("cant not divided zero")
    
# except ValueError:
#     print("value error")

# File Operations----------------------------------------------------->

# with open('SKD.txt','w') as file:
#     file.write("hello world,hi")
# with open('SKD.txt','r') as file:
#     print(file.read())
