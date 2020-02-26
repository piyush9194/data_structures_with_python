import re
def palindrome(string):
    # string = re.split("",string)
    # print(string)
    start = 0
    end = len(string) -1
    while start < end:
        if string[start] == " ":
            start = start +1
        elif string[end] == " ":
            end = end -1
        elif string[start].lower() != string[end].lower():
            print(string[start].lower(),string[end].lower())
            return False
        else:
            start = start +1
            end = end -1
    return True


print(palindrome("  tmada M  "))