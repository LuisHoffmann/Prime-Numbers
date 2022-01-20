## Your code should check if each number in the list is a prime number
check_prime = [1, 2, 3, 4, 5, 6, 7, 11, 26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

for index in range(0, len(check_prime)):
    if check_prime[index] == 1:
        print('1 is NOT a prime number because it has only the factor 1')
        continue
    is_prime = True
    for num in range(2, 10):
        if num < check_prime[index] and check_prime[index] % num == 0 and check_prime[index] != num:
            print('{} is NOT a prime number, because {} is a factor of {}'
            .format(check_prime[index], num, check_prime[index]))
            is_prime = False
            break
    if is_prime:
        print('{} IS a prime number'.format(check_prime[index]))