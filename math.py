#Ian Wong
#5/14/16
#Addition and Subtraction

def add():
    print (int(num1+num2))

def sub():
    print (str(num1-num2))

answer = (input("Would you like to (add/subtract)?"))
num1 = int(input("What is your first number:"))
num2 = int(input("What is your second number:"))

if answer == "add":
     add()

if answer == "subtract":
    sub()

