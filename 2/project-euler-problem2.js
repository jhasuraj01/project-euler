function fiboEvenSum(limit) {
    var fibCache = {
        "1": 1,
        "2": 2
    }

    var fib = (x) => {
        if (Boolean(fibCache[x]) === false) {
            fibCache[x] = fib(x - 1) + fib(x - 2)
        }
        return fibCache[x]
    }

    var sum = 0;
    for (let n = 1; fib(3 * n - 1) <= limit; n++) {
        sum += fib(3 * n - 1);
    }

    return sum
}

fiboEvenSum(10);
