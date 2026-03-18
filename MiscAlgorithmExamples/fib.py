

def fib(n):
    ''' Returns value of nth place in fib sequence'''
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    


#Just an example of putting all to a list, then printing.

numlen = int(input("go:"))

list = []
for i in range (numlen):
    list.append(fib(i))

print(list)