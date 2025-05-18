# pi=3.14159265359
# formated_pi= "value of pi:{:.4f}".format(pi)
# print(formated_pi)

# print('\u21AA')

#condition part ------------------->

a= int(input())
if a>79:
    print("A+")
elif a<80 and a>=33:
    print("Medium")
else:
    print("Sorry!")
    
#Nested conditional part--------------->

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
