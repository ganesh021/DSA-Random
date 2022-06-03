
def deleteMiddleElement (stack, k):
    if k == 1:                      # base condition - to remove the middle element
        stack.pop()
        return
    temp = stack.pop()              # pop one by one until k = 1 i.e. until middle element is reached
    deleteMiddleElement(stack, k-1)
    stack.append(temp)              # append remaining elements one by one

    
    
    
#driver code
stack = [2,3,4,5,6]
k = len(stack)//2 + 1   # given in question - where Kth element from last needs to be removed
deleteMiddleElement(stack, k)
print(stack)
