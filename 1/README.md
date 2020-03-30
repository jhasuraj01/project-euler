# Problem 1: Sum of Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below the provided input number.

## Algorithm(s)

## Solution(s)

### JavaScript
```javascript
const given_input = 1000;

/**
 * 
 * @param {Number} given_input the limiting integer upto which sum of the multiples of 3 or 5 is to be calculated
 * @returns {Number} sum of the multiples of 3 or 5 upto the given input
 */
const sumOfMultiplesOf3Or5 = (given_input) => {

    const t3 = Math.floor(given_input/3);
    const t5 = Math.floor(given_input/5);
    const t15 = Math.floor(given_input/15);

    const S3 = 3*(t3*(t3 + 1))/2;
    const S5 = 5*(t5*(t5 + 1))/2;
    const S15 = 15*(t15*(t15 + 1))/2;

    const result = S3 + S5 - S15;
  
    return result;
}

console.log(sumOfMultiplesOf3Or5(given_input));
// output: 234168
```
### Python
```python
import math
given_input = int(1000)


def sumOfMultiplesOf3Or5(given_input):

    t3 = int(math.floor(given_input / 3))
    t5 = int(math.floor(given_input / 5))
    t15 = int(math.floor(given_input / 15))

    S3 = int(3 * (t3 * (t3 + 1)) / 2)
    S5 = int(5 * (t5 * (t5 + 1)) / 2)
    S15 = int(15 * (t15 * (t15 + 1)) / 2)

    result = int(S3 + S5 - S15)

    return result


print(sumOfMultiplesOf3Or5(given_input))
# output: 234168
```
### C++
### C#
