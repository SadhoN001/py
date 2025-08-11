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

now = datetime.datetime.now() #2025-08-11 10:23:03.750913
today_date =  datetime.date.today() #2025-08-11
today_time =  datetime.datetime.now().time() #10:23:03.750913
custom_datetime =  datetime.datetime(2030,2,20,10,30,0) #2030-02-20 10:30:00
print(now)
print(now.year)
print(now.month)
print(now.day)
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

# from datetime import datetime
# dt = datetime(
#     year = 2019,
#     month = 2,
#     day = 25,
#     hour= 13,
#     minute=5,
#     second=17,
# )
# print(dt)
# current_dt = datetime.now()
# print( current_dt - dt) # 2358 days, 21:42:56.897089
# print(type(current_dt - dt)) #<class 'datetime.timedelta'>

date_str = "25-12-2030 10:45:00"
parse_date = datetime.datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
print(parse_date) #type datetime.datetime

## part 2------------------------------------------------------->
from datetime import datetime, timedelta

today = datetime.today().date()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

print(today)
print(tomorrow)
print(yesterday)
print(type(today), type(tomorrow) ,type(yesterday)) # <class 'datetime.datetime'>

# now = datetime.today()
now = datetime.now()
new_time = now + timedelta(hours=5, minutes=30)
past_time = now - timedelta(hours=5, minutes=30)
print(now, new_time, past_time)
print(now.time(), new_time.time(), past_time.time())

date1 = datetime(2025, 12, 25)
date2 = datetime(2025, 12, 5)
print(date1-date2) #20 days, 0:00:00
print(date1.day+date2.day) #30
print(type(date1-date2)) # <class 'datetime.timedelta'>

import pytz, datetime
from datetime import datetime, UTC
import time

dhaka = pytz.timezone('Asia/Dhaka')
utc = datetime.now(UTC)

print(dhaka)
print(utc.astimezone(dhaka))
print(utc)
# print(pytz.all_timezones)

start = datetime.now()
time.sleep(5)
end = datetime.now()

print(end-start)

# json------------------------------------------>
import json

data = {
    'name' : "Rahim",
    'age' : 30,
    'is_logged_in' : True,
    'test' : None
}
# serialization : python to json----------------->
json_string = json.dumps(data , indent=4)

print(json_string)
print(type(json_string)) #<class 'str'>

#Deserialization : json to python---------------->

data = '{"name" : "Rahim" , "age" : 30, "is_logged_in" : true, "test" : null}'

python_dict = json.loads(data)
print(python_dict)
print(type(python_dict)) #<class 'dict'>




# request handling ------------------------------------------------->

#system

# Request--->(API)---> Response Cycle
# ostad er website account create kori - POST
# Course details dekhar try kori - GET
# ami nijer profile update korte pari - PUT/ PATCH
# ostad kono course delete korte pare - DELETE

import requests
# Get request
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response)
print(response.text)
print(response.status_code) # 200 means ok
print(response.json())

# post request
data = {'userId': 1, 'id': 1, 'title': 'for test'}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json= data )
print(response.status_code) #201 means created
print(response.json())

# update request
data = {'userId': 1, 'id': 1, 'title': 'for test(updated)'}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json= data )
print(response.status_code) #200
print(response.json())

# Delete request
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1" )
print(response.status_code) #200
print(response.json())

