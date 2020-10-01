# Problem 3: Largest prime factor of a Number

### Question
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

## Algorithm(s)

> To Do

## Solution(s)

### JavaScript
```javascript
/**
 * Unique Prime Factors of A Number
 * @param {Number} num - An Integer
 */
const primeFactors = num => {
    /** @type {Array<Number>} Prime Factor Array */
    let pfa = [num]
    let counter = 2
    while (counter <= Math.sqrt(pfa[pfa.length - 1])) {
        if (pfa[pfa.length - 1] % counter === 0) {
            let lastFactor = pfa[pfa.length - 1]
            while (lastFactor % counter === 0) {
                lastFactor = lastFactor / counter
            }
            pfa[pfa.length - 1] = counter
            pfa.push(lastFactor)
        }
        counter++
    }
    if (pfa[pfa.length - 1] === 1) { pfa.pop() }
    return pfa
}

/**
 * Larget Prime Factor of a Number
 * @param {Number} num - An Integer
 * @returns {Number}
 */
const largestPrimeFactor = num => {
    let pfa = primeFactors(num) // prime factors array
    return pfa[pfa.length - 1]
}

console.log(largestPrimeFactor(600851475143)) // output: 6857
```
### Python
```python
def primeFactors(num):
    # @type {Array<Number>} Prime Factor Array
    pfa = [num]
    counter = 2
    while (counter**2 <= pfa[len(pfa) - 1]):
        if (pfa[len(pfa) - 1] % counter == 0):
            lastFactor = pfa[len(pfa) - 1]
            while (lastFactor % counter == 0):
                lastFactor = lastFactor / counter
            pfa[len(pfa) - 1] = counter
            pfa.append(lastFactor)
        counter += 1

    if (pfa[len(pfa) - 1] == 1):
        pfa.pop()
    return pfa

def largestPrimeFactor(num):
    pfa = primeFactors(num) # prime factors array
    return pfa[len(pfa) - 1]

print(largestPrimeFactor(600851475143)) # output: 6857
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
