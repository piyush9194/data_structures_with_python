"""WAP to implement merge sort"""


def merge(left,right):
    i=j= 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        elif right[j] < left[i]:
            result.append(right[j])
            j = j + 1
    while i < len(left):
        result.append(left[i])
        i = i + 1

    while j < len(right):
        result.append(right[j])
        j = j + 1

    return(result)



def merge_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        left,right = arr[:mid],arr[mid:]
        return merge(merge_sort(left),merge_sort(right))




print(merge_sort([8,5,1,3,2]))