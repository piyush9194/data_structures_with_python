def solve(num):
    # Write your code here
    num = str(num)
    start = 0
    end = len(num) - 1

    while start <= end:
        if num[start] == num[end]:
            if start == end or start==end-1:
                return True
            start = start + 1
            end = end - 1
        else:
            return False

print(solve(44))
