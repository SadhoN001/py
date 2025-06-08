                                         # Object Oriented Programming
# What is object-oriented programminh?
# =>A programming pattern based on the concept of "object"
# =>object contain both data(attribute)and methods(function)

# key OOP Principle:
#     ->Encapsulation: public,private
#     ->Inheritance:reusability,hierarchical relationship,
#     ->Polymorphism: Flexibility and Extensibility
#     ->Abstractiom : 

# class--------------------------------------->
# class dog:
#     #constructor
#     def __init__(self,name,age):
#         self.n=name
#         self.age=age
#     #Method
#     def bark(self):
#         return f"{self.n} says woof!age={self.age}"
       
# a=dog("piku",11)
# print(a.bark())# a are object.object connect function
#  #object
# dog1=dog("a","b")
# dog2=dog("x","y")
# print(dog1.bark())
# print(dog2.bark())

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         return f"hi,i am {self.name}.I'm {self.age} old"
#     def greet(self):
#         return ("thank You")

# a=Person("Sadhon",23)
# print(a.display())
# print(a.greet())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def update_age(self, new_age):
#         self.age = new_age

#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# # Creating two objects of the Person class
# person1 = Person("Alice", 25)
# person2 = Person("Bob", 30)
# # Updating the age of person1
# person1.update_age(26)
# # Printing the updated details of both objects
# person1.display_info()
# person2.display_info()

# Single Responsibility Principle (SRP).--------------------------->
## oop part-1 12number slid task 3 
# class Car:
#     def __init__(self, model):
#         self.model = model

#     def drive(self):
#         print(f"{self.model} is being driven.")


# class FuelEfficiencyCalculator:
#     def calculate_fuel_efficiency(self, miles, fuel):
#         if fuel == 0:
#             return 0  # Avoid division by zero
#         return miles / fuel


# # Example usage
# car = Car("Toyota")
# car.drive()

# fuel_calculator = FuelEfficiencyCalculator()
# efficiency = fuel_calculator.calculate_fuel_efficiency(100, 5)
# print(f"Fuel Efficiency: {efficiency} miles per gallon")
