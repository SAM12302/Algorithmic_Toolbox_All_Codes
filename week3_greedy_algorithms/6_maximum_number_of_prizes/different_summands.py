def optimal_summands(n):
    summands = []
    # write your code here
    i = 1
    remaining = n
    """    while i <= n:
        remaining = remaining - i
        if remaining < i:
            summands.append(remaining + i)
            break
        else:
            summands.append(i)
        i = i + 1
    return summands"""
    #changing logic, close but fails test cases


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
