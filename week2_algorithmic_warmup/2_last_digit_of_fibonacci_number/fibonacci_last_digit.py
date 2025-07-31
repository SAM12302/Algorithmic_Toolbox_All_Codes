def fibonacci_last_digit(n):
    previous = 0
    current = 1
    for i in range(2, n + 1):
        temp = current
        current = current + previous
        previous = temp
    return current % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
