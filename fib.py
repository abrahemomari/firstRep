# print fibonacci numbers

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def main():
    fib(1000)

#fuck github
