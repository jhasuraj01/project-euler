/**
 * Why I didn't used Math.floor() function?
 * Read here:- https://stackoverflow.com/a/10133785
 */
 
using System;

class MainClass {

  static int sumOfMultiplesOf3Or5(int given_input) {

    int t3 = given_input/3;
    int t5 = given_input/5;
    int t15 = given_input/15;

    int S3 = 3*(t3*(t3 + 1))/2;
    int S5 = 5*(t5*(t5 + 1))/2;
    int S15 = 15*(t15*(t15 + 1))/2;

    int result = S3 + S5 - S15;

    return result;
  }

  public static void Main (string[] args) {
    Console.WriteLine (sumOfMultiplesOf3Or5(1000));
  }
}
