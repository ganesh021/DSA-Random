
def reverseSatck (stack):
    if len(stack) == 0:
        return
    temp = stack.pop()
    reverseSatck(stack)
    insertAtStart(stack, temp)
    #stack.insert(0, temp)          # this line could have directly inserted at start - thus func insertAtStart would not be required

def insertAtStart (stack, start):
    if len(stack) == 0:
        stack.append(start)
        return
    temp = stack.pop()
    insertAtStart(stack, start)
    stack.append(temp)




# driver code
stack = [1,2,3,4,5]
reverseSatck(stack)
print(stack)
