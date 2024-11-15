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