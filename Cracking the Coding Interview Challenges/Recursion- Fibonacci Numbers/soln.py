def fibonacci(n):

    # Write your code here.
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

n = int(raw_input())
print(fibonacci(n))