import pytest


def fizz_buzz(number):
	if number % 3 == 0 and number % 5 == 0:
		return "Fizz Buzz"
	if number % 3 == 0:
		return "Fizz"
	if number % 5 == 0:
		return "Buzz"
	return number


def fizz_buzz_list(size):
	resposta = []
	for i in range(1, size+1):
		resposta.append(fizz_buzz(i))
	return resposta


if __name__ == "__main__":
	assert fizz_buzz(1) == 1
	assert fizz_buzz(2) == 2
	assert fizz_buzz(3) == "Fizz"
	assert fizz_buzz(5) == "Buzz"
	assert fizz_buzz(15) == "Fizz Buzz"
	assert fizz_buzz_list(35) == [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizz Buzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "Fizz Buzz", 31, 32, "Fizz", 34, "Buzz"]
