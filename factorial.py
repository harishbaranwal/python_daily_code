#Factorial of number using for loop
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        i+=1
    print(f) 
# input the number    
n=int(input())
#print the factorial of number using define function 
factorial(n) 


# Factorial of number using while loop
# def factorial(n):
#     f=1
#     while n>0:
#         f=f*n
#         n=n-1 
#     print(f)
# n=int(input())
# factorial(n)     