def fiboEvenSum(limit):
    fibCache = {
        "1": 1,
        "2": 2
    }

    def fib(x):
        if (str(x) in fibCache) == False:
            fibCache[str(x)] = fib(x - 1) + fib(x - 2)
        return fibCache[str(x)]

    sum = 0
    n = 1
    while (fib(3 * n - 1) <= limit):
        sum = sum + fib(3 * n - 1)
        n = n + 1
    return sum

print(fiboEvenSum(4000000))
# output: 4613732
