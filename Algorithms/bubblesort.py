# Big O(n^2)

def bubble_sort(arr):
    unsorted = True
    while unsorted:
        temp_arr  = arr.copy()
        pointer = 0
        while(pointer<len(temp_arr)-1):
            if temp_arr[pointer]>temp_arr[pointer+1]:
                # temp = temp_arr[pointer+1]
                # temp_arr[pointer + 1] = temp_arr[pointer]
                # temp_arr[pointer] = temp
                [temp_arr[pointer],temp_arr[pointer + 1]] = [temp_arr[pointer+1],temp_arr[pointer]]
            pointer+=1
        print("Temp arr:")
        print(temp_arr)
        print("Real arr:")
        print(arr)
        if arr == temp_arr:
            unsorted=False
        else:
            arr = temp_arr
    return arr


res = bubble_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])
print(res)