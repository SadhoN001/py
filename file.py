file =open('name.txt', 'r')
content= file.read()
print(content)
file.close()

with open('name.txt', 'r') as f:
    content= f.read()
    print(content)
    print(f)
    
with open('name.txt', 'w') as f:
    f.write("hello world\n")
    f.write("im still waiting \n")
    
with open('name.txt', 'a') as f:
    f.write("Sadhon Kumar Dev \n")
    
line=['i love python\n', 'im harder to python\n']
with open('name.txt', 'a') as f:
    f.writelines(line)
    
import os
print(os.path.abspath('name.txt'))
print(os.path.getsize('name.txt'))# byts
if os.path.exists('name.txt'):
    print('file found')
else:
    print('file not found')

import pathlib
file_path= pathlib.Path('name.txt')
print(file_path)
if file_path.exists():
    print('file exists')
else:
    print('file not found')


class FInput:
    def fileInp():
        try:
            with open('ddd.txt','w') as file:
                print("file Founded")
                file.write(input())
        except FileNotFoundError:
            with open('ddd.txt','w') as file:
                print("file not Founded")
                file.write(input())
       
with open('SKD.txt','r') as file:
    print(file.read())

# a=FInput()
FInput.fileInp()
