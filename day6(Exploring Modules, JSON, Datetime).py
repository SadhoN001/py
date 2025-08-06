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











