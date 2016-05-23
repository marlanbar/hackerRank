# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b, n = map(int, raw_input().split())

fibo_list = {}


def fibo_mod(a, b, n):
    global fibo_list
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        if (a, b, n) in fibo_list:
            return fibo_list[a, b, n]
        else:
            fibo_list[a, b, n] = (fibo_mod(a, b, n - 1)) ** 2 + fibo_mod(a, b, n - 2)
            return fibo_list[a, b, n]

print fibo_mod(a, b, n)
