# Reverse a number given by user
# input the number 
a=int(input("Enter a number: "))
x=0
while (a>0):
    b=a%10
    x=x*10+b
    a=a//10
print("Reverse of the number is",x)    
