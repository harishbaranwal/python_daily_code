# print n term of fibonacci sequence using recursion
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
# Input the number of term        
n=int(input("Enter the no. of term: ")) 
if n<=0:
    print("Please enter a positive number") 
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i),end=" ")    # end=" " is used for print the sequence into single line
        
