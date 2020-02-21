""""Write a program to implement insertion sort algorithm"""
# https://www.youtube.com/watch?v=Nkw6Jg_Gi4w&list=PLj8W7XIvO93rJHSYzkk7CgfiLQRUEC2Sq&index=1


def insertion_sort(arr):
    for i in range(0,len(arr)):
        temp = arr[i]
        j =i-1
        while j >0:
            if arr[j] > temp:
                arr[j+1] = arr[j]
            j = j-1
         arr




    print(arr)
    return arr


print(insertion_sort([8,5,1,3,2]))


