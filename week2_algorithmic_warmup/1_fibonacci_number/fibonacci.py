result = []
def fibonacci_number(n):
    result.append(0)
    result.append(1)
    if n < 1:
        return result[0]
    elif n <= 1:
        return result[1]
    else:
        count = result.index(1)
        while count < n:
            next_fib = result[count] + result[count - 1]
            count = count + 1
            result.append(next_fib)
        return result[count]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
