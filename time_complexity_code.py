def find_sum(arr):
    n=len(arr)
    total=0
    for i in range(n):
        total +=arr[i]
        return total 
    
    
for i in range(n):
    for j in range(n):
        print(i,j)
        
def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left <= right:
        mid=(left+right)//2
        if arr[mid] ==target:
            return mid
        elif arr[mid] <target:
            left=mid+1
        else:
            right=mid-1
            return -1
