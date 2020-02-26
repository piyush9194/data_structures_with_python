""""Write a program to implement insertion sort algorithm"""
# https://www.youtube.com/watch?v=Nkw6Jg_Gi4w&list=PLj8W7XIvO93rJHSYzkk7CgfiLQRUEC2Sq&index=1





def insertion_sort(data):
    for i in range(1,len(data)):
        j = i-1
        while j >=0:
            if data[j]>data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                j = j-1
            else:
                break
        print(data)
    return(data)



print(insertion_sort([8,5,1,3,2]))


