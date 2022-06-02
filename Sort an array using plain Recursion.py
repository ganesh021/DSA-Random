arr = [3,5,1,2,4]

def appendInSorted(arr, temp):
    if len(arr) == 0 or arr[-1] <= temp:
        arr.append(temp)
        return
    temp2 = arr.pop()
    appendInSorted(arr, temp)
    arr.append(temp2)

def sort(arr):
    if len(arr) == 1:
        return
    temp = arr.pop()
    sort(arr)
    appendInSorted(arr, temp)

sort(arr)
print(arr)
