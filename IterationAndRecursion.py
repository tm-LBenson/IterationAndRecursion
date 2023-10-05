list_of_numbers = [0,1,5,10,25,50,100]
def interative_approach(list_of_numbers):
    print('Factortial results using an interative approach')
    def iterate_factorial(num):
        total = 1;
        for i in range(1, num + 1):
            total = total * i
        return print(f'{num}! = {total}')
    for num in list_of_numbers:
        iterate_factorial(num)
    

def recursive_approach(list_of_numbers, index=0):
    if index == 0:
        print('Factortial results using an recursive approach')
    if index == len(list_of_numbers):
        return
    def recursive_factoral(num):
        if num in [0,1]:
            return 1
        return num * recursive_factoral(num - 1)
    
    result = recursive_factoral(list_of_numbers[index])
    print(f'{list_of_numbers[index]}! = {result}')
    recursive_approach(list_of_numbers, index + 1)
interative_approach(list_of_numbers)
recursive_approach(list_of_numbers)