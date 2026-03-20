''' 
    Selection Sort
    Time Complexity: O(n2) -> Quadratic Time

'''

def selection_sort(arr):
    '''takes array and returns sorted.'''

    arrlen = len(arr)

    for i in range(arrlen):
        minpos = i
        
        for j in range(minpos, arrlen):
            
            if arr[j] < arr[minpos]:
                minpos = j
    
        arr[i], arr[minpos] = arr[minpos], arr[i]

    return arr

#------------------------------------------------------------


#ignore, this is for testing the function in action. 
sample = [4,6,3,7,8,2,4,7,3,9,5,4,3,]
printer = selection_sort(sample)
print(printer)