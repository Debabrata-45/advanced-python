def sum_of_digits(n):
    n = abs(n)  
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
n = int(input("Enter a number: "))
print(sum_of_digits(n))