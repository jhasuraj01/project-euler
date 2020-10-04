# Problem 5: Smallest multiple

### Question
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

## Algorithm(s)

> To Do

## Solution(s)

### JavaScript
```javascript
/**
 * Prime Factorization of A Number
 * @param {Number} num - An Integer
 */
const primeFactorization = num => {
    /** @type {Array<Number>} Prime Factor Array */
    let pfa = [num]
    let counter = 2
    while (counter <= Math.sqrt(pfa[pfa.length - 1])) {
        while (pfa[pfa.length - 1] % counter === 0) {
            let lastFactor = pfa[pfa.length - 1]
            pfa[pfa.length - 1] = counter
            pfa.push(lastFactor / counter)
        }
        counter++
    }
    if (pfa[pfa.length - 1] === 1) { pfa.pop() }
    return pfa
}

const getSmallestMultiple = (lowerBound, upperBound) => {
    let primeFactorCount = {}
    for (let i = lowerBound; i <= upperBound; i++) {
        const pfa = primeFactorization(i)
        let index = 0
        while (index < pfa.length) {
            const factor = String(pfa[index]) // convert to string for comparing in object
            const lastIndexOfFactor = pfa.lastIndexOf(pfa[index])
            const factorCount = lastIndexOfFactor - index + 1
            
            if (factor in primeFactorCount) {
                primeFactorCount[factor] = Math.max(primeFactorCount[factor], factorCount)
            } else {
                primeFactorCount[factor] = factorCount
            }

            index = lastIndexOfFactor + 1
        }
    }
    
    let smallestMultiple = 1
    for (const factor in primeFactorCount) {
        if (primeFactorCount.hasOwnProperty(factor)) {
            const factorCount = primeFactorCount[factor];
            smallestMultiple *= Math.pow(Number(factor), factorCount)
        }
    }
    console.log(smallestMultiple);
    return smallestMultiple
}

getSmallestMultiple(1, 20) // output: 232792560
```
### Python
```python
def primeFactorization(num):
    pfa = [num]
    counter = 2
    while (counter**2 <= pfa[-1]):
        while (pfa[-1] % counter == 0):
            lastFactor = pfa[-1]
            pfa[-1] = counter
            pfa.append(lastFactor / counter)
        counter += 1
    if (pfa[-1] == 1):
        pfa.pop()
    return pfa

def lastIndex(arr, elm):
    indexFromBack = arr[::-1].index(elm)
    return len(arr) - indexFromBack - 1

def getSmallestMultiple(lowerBound, upperBound):
    primeFactorCount = {}
    for i in range(lowerBound, upperBound + 1):
        pfa = primeFactorization(i)
        index = 0
        while (index < len(pfa)):
            factor = str(int(pfa[index])) # convert to string for comparing in object
            lastIndexOfFactor = lastIndex(pfa, pfa[index])
            factorCount = lastIndexOfFactor - index + 1

            if factor in primeFactorCount:
                primeFactorCount[factor] = max(primeFactorCount[factor], factorCount)
            else:
                primeFactorCount[factor] = factorCount

            index = lastIndexOfFactor + 1

    smallestMultiple = 1
    for factor, factorCount in primeFactorCount.items():
        # factorCount = primeFactorCount[factor]
        smallestMultiple *= int(factor)**factorCount
    return smallestMultiple

print(getSmallestMultiple(1, 20)) # output: 232792560
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