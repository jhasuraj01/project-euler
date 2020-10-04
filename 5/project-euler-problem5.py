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