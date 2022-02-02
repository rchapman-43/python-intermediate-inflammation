# fizzbuzz
"""generate the sequence of integers, 
but replace multiples of three with “Fizz”, 
multiples of five with “Buzz”, 
and multiples of both with “FizzBuzz”."""

# i.e. 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)