""" 
    Linear Search
    Time Complexity: O(n)
    Rationale: All values are searched in a linear fashion

"""


numsearch = int(input("Num to search: "))
fooarray = [1,6,3,5,2,9,4,8,5,3,7,]


def linear_search(n, arr,):
    ''' Takes input of value, list. Returns bool '''

    isFound = False

    for i, num in enumerate(arr):
        if num == n:
            print(f"found an instance of {n} at position[{i}]!")
            isFound = True
    
    if not isFound:
        print("Too bad man...") 
    
    return isFound


linear_search(numsearch, fooarray)