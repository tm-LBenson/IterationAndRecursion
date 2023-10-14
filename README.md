# Factorial Calculation

This program calculates the factorial of a list of numbers using both iterative and recursive approaches.

## List of Numbers

The following list of numbers are used for the factorial calculation:
```py
list_of_numbers = [0,1,5,10,25,50,100]
```
## Iterative Approach

The iterative approach uses a loop to multiply each number from 1 up to the desired number. 
```py
def interative_approach(list_of_numbers):
    print('Factorial results using an iterative approach')
    def iterate_factorial(num):
        total = 1
        for i in range(1, num + 1):
            total = total * i
        return print(f'{num}! = {total}')
    for num in list_of_numbers:
        iterate_factorial(num)
```
## Recursive Approach

The recursive approach multiplies the number with the factorial of the previous number until it reaches 1.
```py
def recursive_approach(list_of_numbers, index=0):
    if index == 0:
        print('Factorial results using a recursive approach')
    if index == len(list_of_numbers):
        return
    def recursive_factorial(num):
        if num in [0,1]:
            return 1
        return num * recursive_factoral(num - 1)
    
    result = recursive_factoral(list_of_numbers[index])
    print(f'{list_of_numbers[index]}! = {result}')
    recursive_approach(list_of_numbers, index + 1)
```
## Execution

To see the results of the factorial calculation for the given list of numbers, execute the following:
```py
interative_approach(list_of_numbers)
recursive_approach(list_of_numbers)
```
