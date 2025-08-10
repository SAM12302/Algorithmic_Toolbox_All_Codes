def binary_search(keys, query):
    # write your code here
    high = len(keys) - 1
    low = 0
    mid = int(low + (high - low)/2)
    if low > high:
        return print()

    if query == keys[mid]:
        return mid
    elif query < keys[mid]:
        return binary_search(keys[:(mid - 1)], query)
    elif query > keys[mid]:
        return binary_search(keys[(mid + 1):], query)



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
