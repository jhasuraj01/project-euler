package main

import (
	"fmt"
)

func sumOfMultiplesOf3Or5(given_input int) int {

	var t3 int = given_input / 3
	var t5 int = given_input / 5
	var t15 int = given_input / 15

	var S3 int = 3 * (t3 * (t3 + 1)) / 2
	var S5 int = 5 * (t5 * (t5 + 1)) / 2
	var S15 int = 15 * (t15 * (t15 + 1)) / 2

	var result int = S3 + S5 - S15

	return result
}

func main() {
	fmt.Println(sumOfMultiplesOf3Or5(1000))
}

// output: 234168
