""""Write a program to implement quick sort"""



def quick_sort(arr):
    pivot = int(len(arr)-1/2)

    start = 0
    end = len(arr)-1
    while start < end:
        if arr[start] > pivot and arr[end] < pivot:

            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start = start +1
            end = end -1

        if arr[start] > pivot and arr[end] > pivot:
            end= end-1
        if arr[start] < pivot:
            start = start +1
        if arr[end] > pivot:
            end = end -1
        print(start, end, arr)

     if start< end:
         quick_sort()


quick_sort([3,9,8, 4 ,1,7,2])


