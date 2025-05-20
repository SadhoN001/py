# pi=3.14159265359
# formated_pi= "value of pi:{:.4f}".format(pi)
# print(formated_pi)

# print('\u21AA')

# # Bitwaise-------------------------->
# a=5
# b=3
# bitwaise_and= a&b
# bitwaise_or= a|b
# bitwaise_xor= a^b
# bitwaise_not_a= ~a

# print("bitwaise_and:", bitwaise_and)#1
# print("bitwaise_or:", bitwaise_or)#7
# print("bitwaise_xor:", bitwaise_xor)#6
# print("bitwaise_not_a:", bitwaise_not_a)#-6

#condition part -------------------------------->

a= int(input())
if a>79:
    print("A+")
elif a<80 and a>=33:
    print("Medium")
else:
    print("Sorry!")
    
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
