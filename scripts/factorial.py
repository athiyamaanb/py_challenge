

def factorial(n):
    if n == 1:
        print('here')
        print(n)
        return n

    return factorial(n-1) * n


print(factorial(6))