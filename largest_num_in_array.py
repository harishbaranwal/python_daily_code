# print largest number in an array
# define a function which calculate the largest number
def largest(arr,n):
    largest_num=arr[0]
    for i in range(1,n):
        if arr[i]>largest_num:
            largest_num=arr[i]
    return largest_num
# input the array
arr=list(map(int,input("Enter the array elements: ").split(","))) 
n=len(arr)
# print the largest number in the given array
print("Largest number in the given array is",largest(arr,n))
# this is end of the program



# this code is use when calculate largest number in floating element array
# def largest(arr,n):
#     largest_num=arr[0]
#     for i in range(1,n):
#         if arr[i]>largest_num:
#             largest_num=arr[i]
#     return largest_num
# arr=list(map(float,input("Enter the array elements: ").split(","))) 
# n=len(arr)
# print("Largest number in the given array is",largest(arr,n))
