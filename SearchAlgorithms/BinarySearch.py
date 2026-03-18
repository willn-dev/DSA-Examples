''' 
    Binary Search
    Time Complexity: O(log n) -> Logarithmic Time
    Rationale: Each operation discards half of the data. 
    Drawbacks: Must be in sorted order before performing

'''
# for example test 
list_to_search = [1,3,5,6,8,31,65,32,56,87,123,125,235,632,1123,4564]
upperstart = len(list_to_search)




def binary_search(n, arr):
    ''' Returns bool. binary_search(target,list)'''

    upper = len(arr) -1
    lower = 0
  
    while lower <= upper:
		
        mid = (lower + upper) // 2 #sets the rounded middle of the list
		
        if(arr[mid] == n):
            print("found")  #is value mid?
            return True
        
        elif (arr[mid] < n): # if its less, the lower bound is cut.
            lower = (mid + 1)
        else:
            upper = (mid - 1) #else upper is cut. 
            
		
    print('not found')
    return False






binary_search(5, list_to_search)