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
    console.log(primeFactorCount,smallestMultiple);
    return smallestMultiple
}

getSmallestMultiple(1, 10) // output: 232792560