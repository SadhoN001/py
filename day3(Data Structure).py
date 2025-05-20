
# python data structure--------------------------------------------------------->
#list----------------------------------------[  ]----------------------->
# An ordered,mutable collection of iteams.

# my_list=[1,2,3,4,5]
# first_element=my_list[0]
# subset=my_list[1:4]
# my_list[2]=10
# my_list.append(6)
# my_list.remove(4)

# print(f'my list: {my_list}')
# print(f'first_element: {first_element}')
# print(f'subset: {subset}')

# import numpy as np
# my_array= np.array([1,2,3,4,5])
# frist_element_np= my_array[0]
# print(f'my numpy array: {my_array}')
# print(f'frist_element_np: {frist_element_np}')

# list=[1,2,3,4]
# print(type(list))
# list.append("skd")#insert/append element in the list
# print(list) ###[1, 2, 3, 4, 'skd']
# list.remove(3)# remove element list <----------------|
# print(list) ###[1, 2, 4, 'skd']
# print(list[3]) ###Access by Index--->skd
# list[0]="change"
# print(list) ###['change', 2, 4, 'skd']
# list.insert(2,200)# insert element list <-------------|
# print(list) ###['change', 2, 200, 4, 'skd']
# print(list.count(100)) ###0
# print(list.index(200)) ###2
# # list.sort(reverse=True)
# # print(list)
# # s=sorted(list)
# # print(s)
# print(len(list)) ###5

# n=int(input("Enter the number: "))
# l=[]
# for i in range(n):
#     l.append(input())
# print(l)

# user_inp=input("Enter item separated by comma: ") # apple,banana,mango
# l=user_inp.split(",")
# print(l)

# user_inp=input("Enter item separated by space: ") # 1 2 3 4
# l=list(map(int,user_inp.split()))# only int [str...etc]
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

# list=[
#     {
#     "id": 1,
#     "name": "Yamaha R15 V4",
#     "brand": "Yamaha",
#     "description": "A premium sports bike with advanced technology and sleek design.",
#     "price": 420000,
#     "rating": 4.7,
#     "image": "https://images.hindustantimes.com/auto/img/2022/05/11/1600x900/2021-Yamaha-R15-V4-Monster-Energy-MotoGP-Edition-Front-Quarter_1652236418830_1652236426891.jpg\n"
#   },
#   {
#     "id": 2,
#     "name": "Honda CBR 150R",
#     "brand": "Honda",
#     "description": "A well-balanced motorcycle offering comfort, speed, and fuel efficiency.",
#     "price": 400000,
#     "rating": 4.5,
#     "image": "https://www.motorbeam.com/wp-content/uploads/Honda-CBR150R-Test-Ride-Review.jpg"
#   }]

# for i in list:
#     for x,y in i.items():
#         print(f"{x}:{y}")

#Tuple-----------------------------------------(  )------------------------->
# An immutable, ordered collection if items. 
## can not be append ,insert,change beacause immutable.

# my_tpl=(1,2,'a','b')
# print(type(my_tpl))
# print(my_tpl)
# print(my_tpl[1])
## my_tpl[0]="ch"
## print(my_tpl)# it show Traceback, because tuple immutable

# a=(1,2,3)
# x,y,z=a
# print(x,y,z)

# n=(1,2,3,4,5)
# first,*rest,last=n
# print(first,rest,last) ### 1 [2, 3, 4] 5

# a=(1,2,3)
# b=(4,5,6)
# c=a+b
# print(c) ### (1, 2, 3, 4, 5, 6)
# c=a*2
# print(c) ### (1, 2, 3, 1, 2, 3)

# name=('a','b','c')
# age=('1','2','3')
# result_tuple= tuple(zip(name,age))
# print(result_tuple) ###(('a', '1'), ('b', '2'), ('c', '3'))

# t=(1,2,2,3,4,2,5)
# cnt=t.count(2) 
# print(cnt)#3
# s=sorted(t)
# print(s) # [1, 2, 2, 2, 3, 4, 5]
# print(type(s))#list
# l=len(t)
# print(l) # 7
# sorted(t)
# print(t)#(1, 2, 2, 3, 4, 2, 5)
# print(type(t))#tuple
# t=(10,20,30,40,50,60,70,80)
# i=t.index(30) # 2
# print(i)

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


# my_set={10,20,30,40,50}
# for index, value in enumerate(my_set):
#     print(f"index: {index} , value: {value}")

# my_set={10,20,30,40,50}
# while my_set:
#     item=my_set.pop()
#     print(item)

# set1={1,2,3,4}
# set2={4,5,6}
# rslt_set=set1.union(set2)
# print(rslt_set) ###{1, 2, 3, 4, 5, 6}
# rslt_set=set1 | (set2)
# print(rslt_set) ###{1, 2, 3, 4, 5, 6}
# rslt_set=set1.intersection(set2)
# print(rslt_set) ###{4}
# rslt_set=set1 & (set2)
# print(rslt_set) ###{4}
# rslt_set= set1.issubset(set2)
# print(rslt_set)

# my_set={30,60,90}
# my_set.add(100)
# print(my_set)       ###{100, 90, 60, 30}
# my_set.update({10,20,50})
# print(my_set)       ### {50, 10, 100, 20, 90, 60, 30}
# my_set.remove(30)
# print(my_set)       ### {50, 10, 100, 20, 90, 60}
# my_set.discard(60)
# print(my_set)       ### {50, 10, 100, 20, 90}
# my_set.clear()
# print(my_set) #empty


# dictionary----------------------{ key : value }-------------------------------->
# A collection of Key-Value Pair

# my_dict={'name':"skd", 'age':'25', 'city':'bangladesh'}
# del my_dict['age']
# print(my_dict) #{'name': 'skd', 'city': 'bangladesh'}
# print(my_dict['name']) #skd
# my_dict.clear()
# print(my_dict) #{}

# my_dict={'name':"skd", 'age':'25', 'city':'bangladesh'}
# keys=my_dict.keys()
# print(keys) # dict_keys(['name', 'age', 'city'])
# values=my_dict.values()
# print(values) # dict_values(['skd', '25', 'bangladesh'])
# items= my_dict.items()
# print(items) #dict_items([('name', 'skd'), ('age', '25'), ('city', 'bangladesh')])
# age=my_dict.get('age')
# print(age) #25
# remove_age= my_dict.pop('age')
# print(remove_age) #25
# print(my_dict) # {'name': 'skd', 'city': 'bangladesh'}
# new_data={'age':30,'hobby':'playing'}
# my_dict.update(new_data)
# print(my_dict) # {'name': 'skd', 'city': 'bangladesh', 'age': 30, 'hobby': 'playing'}


# my_dict={'name':"skd", 'age':'25', 'city':'bangladesh'}
# for key in my_dict:
#     print(key)
    
# for value in my_dict.values():
#     print(value)
    
# for key,value in my_dict.items():
#     print(f"{key} : {value}")

# person={
#     'name':"skd",
#     'age':'25',
#     'address':{
#         'city':'bangladesh',
#         'zipcode':"2410"
#     }
# }
# print(person)
# print(person['address']['city']) #bangladesh
# person['address']['zipcode']='1111'
# print(person['address']['zipcode']) #1111


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
