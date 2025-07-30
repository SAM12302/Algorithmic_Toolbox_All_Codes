result = []
def fibonacci_last_digit(n):
    if n < 1:
        return n
    elif n <= 1:
        return n
    else:
        result.append(0)
        result.append(1)
        count = result.index(1)
        while count < n:
            next_fib = result[count] + result[count - 1]
            count = count + 1
            result.append(next_fib)
    return next_fib % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
