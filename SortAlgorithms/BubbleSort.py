''' 
    Bubble Sort
    Time Complexity: O(n2)

'''

def bubble_sort(arr):
    ''' call as bubble_sort(arr) and arr is modified in place.'''
    for i in range (len(arr)-1, 0, -1): #counts down from the length of array.
        swapped = False
        for j in range(i): # i shrinks each iteration because final value is solved
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


# Example
nums = [1,5,3,2,65,32,23,12,2,5,6,]
bubble_sort(nums)

print(nums)