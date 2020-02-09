def has_pair_with_sum(list,num):
    start= 0
    end=len(list)-1

    while start <=end:
        s= list[start]+list[end]
        if s > num:
            end=end-1
        elif s < num:
            start= start+1
        elif s  == num:
            return True
    print("not found")
    return False


print(has_pair_with_sum([1,3,5,6,78,90],9))


