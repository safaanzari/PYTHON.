def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("please select the options")
print("a.  additon")
print("b.  subtraction")
print("c.  multiplication")
print("d.  division")
choice=input("please enter your choice -a,b,c,d")
num1=int(input("enter your first number"))
num2=int(input("enter your second number"))
if choice=="a":
    print(add(num1,num2))
elif choice=="b":
    print(sub(num1,num2))
elif choice=="c":
    print(mul(num1,num2))
elif choice=="d":
    print(div(num1,num2))
else:
    print("invalid number")
   




