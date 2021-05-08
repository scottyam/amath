import random

global coefficients
global degree
global guesses
global denominator_result
coefficients = []
degree = int(input("Input the degree of the function:"))
guesses = []
denominator_result = 1.0

def input_coefficients(degree, coefficients):
    for i in range(degree + 1):
        print("x ^", abs(i - degree))
        enter_coefficients = float(input())
        coefficients.append(enter_coefficients)
    return coefficients
    
def make_guesses(degree):
    for i in range(degree):
        guesses.append((float(random.randint(-100, 100)) + 1j))
    return guesses

def value_of_the_function(coefficients, degree, x):
    result = 0.0
    for i in range(degree + 1):
        if i < (degree + 1):
            result += (coefficients[i]) * pow(x, (degree - i))
        if i == (degree + 1):
            result += (coefficients[i])
    return result

def error():
    value = 0.0
    for i in range(degree - 1):
        value += value_of_the_function(coefficients, degree, guesses[i])
    return abs(value)

def denominator(denominator_result, coefficients, x):
    for i in range(degree):
        if guesses[i] != x:
            denominator_result *= (x - (guesses[i]))
    denominator_result *= (coefficients[0])
    return denominator_result

def main():
    input_coefficients(degree, coefficients)
    make_guesses(degree)

    while error() > 0.0000000000001:
        for i in range(degree):
            guesses[i] = guesses[i] - (
                value_of_the_function(coefficients, degree, guesses[i]) / denominator(denominator_result, coefficients, guesses[i])
            )
    for i in range(degree):
        if round(guesses[i].imag, 10) != 0j:
            guesses[i] = (round(guesses[i].real, 10) + round(guesses[i].imag, 9)*1j)
        else:
            guesses[i] = round(guesses[i].real, 10)
    return guesses

print(main())