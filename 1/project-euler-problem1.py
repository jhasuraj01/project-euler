import math
given_input = int(8456)


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
