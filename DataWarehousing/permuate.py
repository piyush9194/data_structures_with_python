# def permuate(data,l,r):
#     if l==r:
#         print(''.join(data))
#     else:
#         for i in range(l,r+1):
#             data[l],data[i]=data[i],data[l]
#             permuate(data,l+1,r)
#             data[l],data[i]=data[i],data[l]
#
# data= 'abc'
# permuate(list(data),0,len(data)-1)



def remove_dup(list):
    seen = set()
    result = []
    dups=[]

    for item in list:
        if item not in seen:
            seen.add(item)
            result.append(item)
        else:
            dups.append(item)
    print(f"dups are {dups}")
    return(result)

print(remove_dup([1,2,3,4,5,7,3,4,2,1]))






