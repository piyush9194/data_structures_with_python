import re
def isPalindrome(data):
    print(data)
    result = ""
    if len(data)<=1:
        # print("Inside")
        result = "Yes"
        print(result)
        return(result)
    else:
        if data[0] == " ":
            isPalindrome(data[1:])
        if data[-1] == " ":
            isPalindrome(data[:-1])
        elif data[0] != data[-1]:
            # print("incomplete")
            result = "No"
            return result
        else:
            # print("recursive")
            isPalindrome(data[1:-1])



print(isPalindrome("  madam  "))










# words = re.findall(r"[\w']+", data)