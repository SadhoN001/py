pi=3.14159265359
formated_pi= "value of pi:{:.4f}".format(pi)
#formated_pi= round(pi,4)
print(formated_pi)

print('\u21AA')

# # Bitwaise-------------------------->
a=5
b=3
bitwaise_and= a&b
bitwaise_or= a|b
bitwaise_xor= a^b
bitwaise_not_a= ~a

print("bitwaise_and:", bitwaise_and)#1
print("bitwaise_or:", bitwaise_or)#7
print("bitwaise_xor:", bitwaise_xor)#6
print("bitwaise_not_a:", bitwaise_not_a)#-6

#condition part -------------------------------->

a= int(input())
if a>79:
    print("A+")
elif a<80 and a>=33:
    print("Medium")
else:
    print("Sorry!")


str = input(" ")

# cnt1 = user_input.count("cat")
# cnt2 = user_input.count("hat")
#print(cnt1 , cnt2)

if str.count("cat") == str.count("hat"):
    print(True)

else:
    print(False)
    
#Nested conditional part----------------------------->

# a=int(input())
# if a>=33:
#     if a>=70:
#         print("A")
#     elif a>=60:
#         print("B")
#     else:
#         print("C")
# else:
#     print("Fail")

#loop----------------------------------->

# for i in range(5):
#     print(i)

# cnt=1
# while cnt<11:
#     print("2 *",cnt,"=",2*cnt)
#     cnt=cnt+1    

# n=int(input())
# i=1
# while i<=10:
#     print(f"{n} X {i} = {n*i}")
#     i=i+1

# total=0
# while True:
#     user_imput= input("enter number (exit then stop): ")
#     if user_imput.lower()== 'exit':
#         print(f"total:{total}")
#         break
#     total+=int(user_imput)

# name="skd"
# age=24
# output= "person:{}, age: {}.".format(name,age)
# print(output)

# name="skd"
# age=24
# output= "person:{0}, age: {1}.".format(name,age)
# print(output)

# Break and Continue--------------------------> 
# for i in range(10):
#     if i==5:
#         break
#     print(i)
    
# for i in range(11):
#     if i%3==0:
#         continue
#     print(i)

# function----------------------------------------->

# def Genfactorial(n):# function pass in parameter
#     if n==0:
#         return 1#the base case if n==0 then condition true and return 1 
#     else:
#         return n*Genfactorial(n-1)# n* recursive called factoril (n-1)

# x=Genfactorial(int(input()))#function call or pass the value and return value store in x
# print(x)# print the value of x

## vowel count
def Vowel_cnt(input_str):
    vowel="aeiouAEIOU"
    return sum(1 for char in input_str if char in vowel)
x="aaa"
print(Vowel_cnt(x))

#multiple argument-->
def add(*args):
    print(args)
    return (sum(args))
    
r=add(1,2,3,4)
print(r)

#keyword argument--->
def fun(**kwargs):
    print(kwargs)
    print(f"my name is {kwargs['f_name']} {kwargs['l_name']} and age {kwargs['age']}\n mark={kwargs['mark']} ")
    
fun(age=25, l_name="dev",mark=95,f_name="Sadhon Kumar")

##lambda ----------------------> anonymous function
#lambda function print korte pare na..return korte pare
sqr=lambda x: x*x
print(sqr(4))

add= lambda a,b:a+b
print(add(5,7))

student= [('rahim',60),('karim',49),('fahim',100)]
sorted_student= sorted(student, key= lambda x: x[1])
print(sorted_student)

## map------------------->
nums=[1,2,3,4]

sq_num= list(map(str,nums))
print(sq_num)
sq_num= list(map(float,nums))
print(sq_num)
sq_num= list(map(lambda x: x*x , nums))
print(sq_num)


# ## filter----------------->
even= list(filter(lambda x: x%2==0 ,nums))
print(even)

# import functools
# ## reduce---------------->
sum= functools.reduce(lambda x,y : x+y , nums )
print(sum)

# scope------------------->
# LEGB( local enclosing global built in scope)

n = "Global"  # Global variable

def outer():
    n = "enclosing"  # enclosing variable
    def inner():
        global n
        # nonlocal n
        n = "local"  # local variable
        print(n)#local 2nd
    print(n)# enclosing 1st
    inner()
    print(n)# enclosing 3rd

outer()
print(n)# local




# learn modeul part------------------------------------->

# import math
# print(math.sqrt(16))

# from math import sqrt
# print(sqrt(36))

# import test1
# print(test1.cel_far(37))
# print(test1.area_cir(5))

# from test1 import cel_far,area_cir
# print(cel_far(38))
# print(area_cir(5))
