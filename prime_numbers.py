## Your code should check if each number in the list is a prime number

check_prime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 26, 39, 51, 53, 57, 79, 85]


# The solution from the course:

for num in check_prime:
    # The next code line below excludes number 1 and 2 where 2 is a prime number and 1 not (1 has only one factor)
    # Also it is very unefficient with high numbers. I think it would only be neccessary to check for the numbers from 2 to 7 if you use range(x, y)
    for i in range(2, num):
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break
        if i == num -1:    
            print("{} IS a prime number".format(num))


# I think this would be one solution:

for index in range(0, len(check_prime)):
    if check_prime[index] == 1:
        print('1 is NOT a prime number because it has only the factor 1')
        continue
    is_prime = True
    for num in range(2, 8):
        if num < check_prime[index] and check_prime[index] % num == 0 and check_prime[index] != num:
            print('{} is NOT a prime number, because {} is a factor of {}'
            .format(check_prime[index], num, check_prime[index]))
            is_prime = False
            break
    if is_prime:
        print('{} IS a prime number'.format(check_prime[index]))