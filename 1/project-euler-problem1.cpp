#include <iostream>
#include <cmath>

int sumOfMultiplesOf3Or5(int given_input) {

    int t3 = floor(given_input/3);
    int t5 = floor(given_input/5);
    int t15 = floor(given_input/15);

    int S3 = 3*(t3*(t3 + 1))/2;
    int S5 = 5*(t5*(t5 + 1))/2;
    int S15 = 15*(t15*(t15 + 1))/2;

    int result = S3 + S5 - S15;

    return result;
}

int main() {
  std::cout << sumOfMultiplesOf3Or5(1000);
  return 0;
}

// output: 234168
