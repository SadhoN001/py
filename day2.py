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

# Break and Continue--------------------------> 
# for i in range(10):
#     if i==5:
#         break
#     print(i)
    
# for i in range(11):
#     if i%3==0:
#         continue
#     print(i)