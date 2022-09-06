import numbers


array=[8,7,6,1,0,9,2]
def partation(array,r_index,l_index):
    pevot=array[r_index]
    j=l_index
    for i in range(l_index,r_index):
        # print(j)
        if(array[i]<=pevot):
            array[j],array[i]=array[i],array[j]
            j+=1
    array[j],array[r_index]=array[r_index],array[j]
    return j
def quicksort(array, r_index,l_index):
       
        if l_index>=r_index:
            return
        else:
            pivot_index=partation(array,r_index,l_index)
            # print(l_index,r_index,pivot_index)
            quicksort(array,pivot_index-1,l_index)
            quicksort(array,r_index,pivot_index+1)

quicksort(array,len(array)-1,0)
print(array)