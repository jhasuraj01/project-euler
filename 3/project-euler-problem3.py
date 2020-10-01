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
