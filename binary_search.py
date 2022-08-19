def binary_search(arr,target):
    low=0
    high=len(arr)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if(arr[mid]>target):
            high=mid-1
        elif(arr[mid]<target):
            low=mid+1
        else:
            return mid
    # print(mid)
    return -1
target=int(input("enter the target value to find"))
arr=[1,2,4,5,6,7,8]
pos=binary_search(arr,target)
if(pos>0):
    print("the element is at",pos)
else:
    print("element is not found")