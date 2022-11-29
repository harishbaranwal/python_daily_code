# Check the user given number is palindrome or not
n=int(input("Enter a psoitive number: "))
dup=n
rev=0
while n>0:
    m=n%10
    rev=rev*10+m
    n=n//10
if dup==rev:
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")        
