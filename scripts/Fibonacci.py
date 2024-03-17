# 1,1,2,3,5,8,13,21

# using loop
# time complexity - o(n)
n = 8
a = 0
b = 1
for i in range(0, n):
    print(a)
    c = a + b
    a = b
    b = c

print('----')




def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n ==0:
        return 0
    return fib(n-1) + fib(n-2)

print(fib(8))
