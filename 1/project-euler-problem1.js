const given_input = 19564;

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
