

def subarray(data,duration):
    result = []
    
    for i in range(0,len(data)):
        j=i
        sum=0
        j=i
        while j>=0 and j>=i-duration+1:
            print(data[j],end=' ')
            sum+=data[j]
            j=j-1
        print(sum)
        result.append(sum%3)  
    print(result)

a = [3,2,9,1,5,2,3,4]
subarray(a,3)    
            
            
            