# Problem 6: Sum square difference

### Question
The sum of the squares of the first ten natural numbers is,
1<sup>2</sup> + 2<sup>2</sup> + ... + 10<sup>2</sup> = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)<sup>2</sup> = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.

## Algorithm(s)

> To Do

## Solution(s)

### JavaScript
```javascript
const sumSquareDifference = n => {
    return (3 * Math.pow(n, 4) + 2 * Math.pow(n, 3) - 3 * Math.pow(n, 2) - 2 * n) / 12
}

console.log(sumSquareDifference(100)) // output: 25164150
```
### Python
```python
def sumSquareDifference(n):
    return (3 * n**4 + 2 * n**3 - 3 * n**2 - 2 * n) / 12

print(sumSquareDifference(100)) # output: 25164150
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
