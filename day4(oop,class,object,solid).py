                                         # Object Oriented Programming
# What is object-oriented programminh?
# =>A programming pattern based on the concept of "object"
# =>object contain both data(attribute)and methods(function)

# key OOP Principle:
#     ->Encapsulation: public,private
#     ->Inheritance:reusability,hierarchical relationship,
#     ->Polymorphism: Flexibility and Extensibility
#     ->Abstractiom : 

# class and Object--------------------------------------->

# __init__(): Dunder merhod, Constructor, no return
# constructor 3 type 
# 1. Default Constructor
# 2.Parameterized Constructor
# 3.Default value Constructor

class Car:
    def __init__(self): 
        self.brand=""
        self.model=""
    # def __init__(self, brand, model): 
    #     self.brand= brand
    #     self.model= model
    # def __init__(self, brand="toyota", model="corolla"): 
    #     self.brand= brand
    #     self.model= model
    
### 1. Default Constructor     
car1=  Car()
car1.brand='toyota'
car1.model='Corolla'
print(car1.brand)
print(car1.model)

car2=  Car()
car2.brand='Honda'
car2.model='civic'
print(car2.brand)
print(car2.model)

##2 Parameterized Constructor
# car=  Car('toyota','corola')
# print(car.brand)
# print(car.model)

# 3.Default value Constructor
# car=Car()
# print(car.brand,car.model)


class Employee:
    company_name="skd company"
    def __init__(self, name, salary):
        self.name= name
        self.salary= salary
        
    def display_info(self): # instance method
        print(f"EMP name : {self.name}\nSalary : {self.salary}")
        
    @classmethod
    def change_company_name(cls, name):# class method
        cls.company_name= name
        
ob1= Employee("Sadhon", 3000)
ob1.display_info()
# ob1.change_company_name("jkd company")
Employee.change_company_name("jkd company")
print(ob1.company_name)


### static method
class School:
    school_name= "ABC school"
    
    @staticmethod
    def calculate_grade(marks):
        if 90<=marks:
            return "A+"
        else:
            return "F"
        
print(School.calculate_grade(99))
        


class dog:
    #constructor
    def __init__(self,name,age):
        self.n=name #instance variable
        self.age=age
    #Method
    def bark(self): #instance methoad
        return f"{self.n} says woof!age={self.age}"
       
a=dog("piku",11)
print(a.bark())# a are object.object connect function
 #object
dog1=dog("a","b")
dog2=dog("x","y")
print(dog1.bark())
print(dog2.bark())

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        return f"hi,i am {self.name}.I'm {self.age} old"
    def greet(self):
        return ("thank You")

a=Person("Sadhon",23)
print(a.display())
print(a.greet())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def update_age(self, new_age):
        self.age = new_age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating two objects of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
# Updating the age of person1
person1.update_age(26)
# Printing the updated details of both objects
person1.display_info()
person2.display_info()




