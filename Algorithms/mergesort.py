def mergesort(arr):
    length = len(arr)
    if(length==1):
        return arr

    mid = length//2
    left = arr[:mid]
    right = arr[mid:]

    return merge(mergesort(left),mergesort(right))

def merge(arr1,arr2):
    temp = []
    p1 = 0
    p2 = 0
    while(p1<len(arr1) and p2<len(arr2)):
        if(arr1[p1]<=arr2[p2]):
            temp.append(arr1[p1])
            p1+=1
        else:
            temp.append(arr2[p2])
            p2+=1
    temp = temp + arr1[p1:] + arr2[p2:]
    return temp

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0,11];

res = mergesort(numbers)

print(res)
