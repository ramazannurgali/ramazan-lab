1.
def generate_squares(N):
    for i in range(N + 1):
        yield i ** 2

# Example usage:
N = int(input("Enter a number (N): "))
for square in generate_squares(N):
    print(square, end=" ")

2.
def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number (n): ")
even_numbers = even_numbers_generator(n)
print(','.join(map(str, even_numbers)))

3.
def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number (n): ")
divisible_numbers = divisible_by_3_and_4_generator(n)
for num in divisible_numbers:
    print(num, end=" ")

4.
def squares_generator(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))
for square in squares_generator(a, b):
    print(square, end=" ")

5.
def count_down(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number (n): ")
for num in count_down(n):
    print(num, end=" ")
