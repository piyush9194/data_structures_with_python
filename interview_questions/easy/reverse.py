"""":arg
Input: "The cat in the hat"
Output: "ehT tac ni eht tah"



"""


def reverse(a):
    a=a.split(" ")
    for i in range(0,len(a)):
        a[i]=a[i][::-1]
    a= " ".join(a)
    return a






a=reverse("The cat in the hat")
print(a)