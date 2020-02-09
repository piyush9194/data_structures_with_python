def show_excitement(data):
    # Your code goes here!
    i=1
    a=""
    while(i<=5):
        a=a+str(data)+" "
        i=i+1
    return a[:-1]

print(show_excitement(data="I am super excited for this course!"))