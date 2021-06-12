def selection_sort(arr):
    final = []
    for i in range(len(arr)):
        smallest = arr[i]
        smallest_i = i
        for j in range(i,len(arr)):
            if(arr[j]<smallest):
                smallest = arr[j]
                smallest_i = j
        [arr[i],arr[smallest_i]] = [arr[smallest_i],arr[i]]
        final.append(smallest)
    return final

print(selection_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))