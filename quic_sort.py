import numbers


array=[8,7,6,1,0,9,2]
def partation(array,r_index,l_index):    #partation code to put pevot in correct position
    pevot=array[r_index]
    j=l_index
    for i in range(l_index,r_index):
        if(array[i]<=pevot):
            array[j],array[i]=array[i],array[j]   #swaping less than pivot to left 
            j+=1
    array[j],array[r_index]=array[r_index],array[j]   #swaping pivot to correct position
    return j
def quicksort(array, r_index,l_index):          
       
        if l_index>=r_index:
            return
        else:
            pivot_index=partation(array,r_index,l_index)
            quicksort(array,pivot_index-1,l_index)         #dividing array based on pivot position
            quicksort(array,r_index,pivot_index+1)

quicksort(array,len(array)-1,0)
print(array)