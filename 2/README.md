# Problem 2: Sum of Even Fibonacci numbers

### Question
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed given ***limit***, find the sum of the even-valued terms.

## Algorithm(s)

> To Do

## Solution(s)

### JavaScript
```javascript
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

fiboEvenSum(4000000)
// output: 4613732
```
### Python
```python
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
```
### C++
```cpp
// To Do
```
### C#
```c#
// To Do
```
### GoLang
```go
// To Do
```