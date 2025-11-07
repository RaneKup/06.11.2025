# задача 1
n = int(input())

def a(x):
    if x < n:
        print(x)
        a(x+1)
a(1)

# задача 2
def check(current_num, target_num, step):
    print(current_num)
    if current_num == target_num:
        return
    check(current_num + step, target_num, step)

A = int(input())
B = int(input())

if A < B:
    step = 1
else:
    step = -1

check(A, B, step)

# задача 3
def deg(n):
    if n == 1:
        return True
    elif n <= 0 or n % 2 != 0:
        return False

    return deg(n // 2)

N = int(input())

if deg(N):
    print("YES")
else:
    print("NO")

#задача 4
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

num = int(input())
result = fib(num)
print(f'элемент {num} равен {result} в числе фебоначи')
