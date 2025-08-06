# demo.py
import demo
print(demo.add(1,2))

from demo import add
# from demo import add as a, mul as m
print(add(2,2))

import random
# help(random)
# print(dir(random))
# print(random.__doc__)
print(random.random()) # 0-1 float er modhhe thakbe
print(random.uniform(5,10))
print(random.randint(11,20))
print(random.randrange(11,20,2))

fruits = ['apple', 'banana', 'cherry']
print(random.choice(fruits))
random.shuffle(fruits)
print(fruits)

def generate_pin():
    return random.randint(1000,9999)

print(f"your 4 digit pin : {generate_pin()}")

# collection module

import collections

# print(collections.__doc__)
# print(dir(collections))

fruits=['apple', 'banana', 'apple', 'orrange']
print(collections.Counter(fruits))
print(collections.Counter(fruits).most_common(2))

word_dic = collections.defaultdict(list)
word_dic['python'].append('programming language')
print(word_dic)

# Datetime----------------------------------------------------------->
import datetime

now = datetime.datetime.now()
today_date =  datetime.date.today()
today_time =  datetime.datetime.now().time()
custom_datetime =  datetime.datetime(2030,2,20,10,30,0) #2030-02-20 10:30:00
print(now)
print(today_date)
print(today_time)
print(custom_datetime)

formatted_date = now.strftime("%Y/%m/%d %H:%M:%S")    # 25/08/06 11:20:22
formatted_date = now.strftime("%y/%m/%d %H:%M:%S")    # 25/08/06 11:20:12
formatted_date = now.strftime("%y/%B/%d %H:%M:%S")    # 25/August/06 11:20:00
formatted_date = now.strftime("%y/%b/%d %A %H:%M:%S") # 25/Aug/06 Wednesday 11:19:18
formatted_date = now.strftime("%y/%b/%d %a %H:%M:%S") # 25/Aug/06 Wed 11:19:18
formatted_date = now.strftime("%y/%b/%d %a %I:%M:%S %p") # 25/Aug/06 Wed 11:22:18 AM
print(formatted_date) #type----> str

date_str = "25-12-2030 10:45:00"
parse_date = datetime.datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
print(parse_date) #type datetime.datetime










