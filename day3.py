
# python data structure--------------------------------------------------------->
#list----------------------------------------[  ]----------------------->
# An ordered,mutable collection of iteams.

# list=[1,2,3,4]
# print(type(list))
# list.append("skd")#insert/append element in the list
# print(list)
# list.remove(3)# remove element list
# print(list)
# print(list[3])#Access by Index
# list[0]="change"
# print(list)

# n=int(input())
# l=[]
# for i in range(n):
#     l.append(input())
# print(l)

# user_inp=input("Enter item separated by comma:")
# l=user_inp.split(",")
# print(l)

# user_inp=input("Enter item separated by space:")
# l=list(map(int,user_inp.split()))# only int 
# print(l)

# def l_sum(a):
#     sum=0
#     for i in a:
#         sum=sum+i
#     return sum
# def larg(a):
#     lar=0
#     for i in a:
#         if(lar<i):
#             lar=i
#     return lar
# def sml(a):
#     sm=999999999
#     for i in a:
#         if(sm>i):
#             sm=i
#     return sm
        
# list1=[1,2,3,4,3]
# x=l_sum(list1)
# print(x)
# y=larg(list1)# function call and find max
# print(y)
# y=max(list1)# max stl
# print(y)
# y=sml(list1)# function call and find min
# print(y)
# y=min(list1)# min stl
# print(y)

#Tuple-----------------------------------------(  )------------------------->
# An immutable, ordered collection if items. 

# my_tpl=(1,2,'a','b')
# print(type(my_tpl))
# print(my_tpl)
# print(my_tpl[1])
# my_tpl[0]="ch"
# print(my_tpl)# it show Traceback, because tuple immutable

# def t_sum(a):
#     sum=0
#     for i in a:
#         sum=sum+i
#     return sum
# tup=(1,2,3,4,5)
# x=t_sum(tup)
# print(x)


# tup=(1,2,3,4,5)
# tup[0]=10
# print(tup)# immutable. it show traceback

# set-----------------------------------{  }-------------------------------------->
# An immutable, unordered collection of unique elements. 

# a={1,2,3,1,2,1,2}
# print(a)

# a={1,2,3}
# b={2,3,4}
# c=a.intersection(b)
# print(c)
# c=a.symmetric_difference(b)
# print(c)

# a={'a','b'}
# print(type(a))# set
# a=list(a)
# print(type(a))# list
# a.append('c')
# print(a)# a b c
# a=set(a)
# print(a)# c a b
# a.remove('a')
# print(a)


# dictionary----------------------{ key : value }-------------------------------->
# A collection of Key-Value Pair

# # a={"a":10,"b":20,"c":30}# dictionary key and value
# a={}
# n=int(input("number of student:"))
# for i in range(n):
#     name=input("inter student name:")
#     score=int(input(f"inter {name} score:"))
#     a[name]=score
# print(a)
# print( f" {(sum(a.values())/len(a)):.5f} " ) # a.value are show dic values in 5 digit decimal

# print(max(a.values()))#max values print
# print(min(a.values()))#min values print

# #list comprehension------------------------------------------------------------>
# A concise way to create list.

# lst=[i*i for i in range(10) if(i%2==0)]
# print(lst)

# # lambda----------------------------------------------------------------------->
# A small anonymous function --> lamda argument : expression

# add= lambda x,y:x+y
# print(add(5,2))

# #list comprehension
# lst=[i for i in range(1,51) if(i%2==0)]
# print(lst)

# #lamba function
# x_mult=lambda x:x*3
# for i in lst:
#     print(x_mult(i),end=" ")#print all even*3

# print(5==4)
