from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.0
    weight = 0.0
    goodness_list = []
    # write your code here
    """n = 4, capacity = 50
    item1: value = 60, weight = 10
    item2: value = 100, weight = 20
    item3: value = 120, weight = 30"""
    for v, w in zip(values, weights):
        goodness = v/w
        goodness_list.append((goodness, v, w))

    goodness_list.sort(reverse=True)
    for goodness, v, w in goodness_list:
        if weight + w <= capacity:
            value = value + v
            weight = weight + w
        else:
            remaining_capacity = capacity - weight
            value = value + goodness * remaining_capacity
            break          

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    """    n = 3  # No more than 3 items
    capacity = 50  # Example knapsack capacity
    values = [60, 100, 120]  # Example item values
    weights = [10, 20, 30]  # Example item weights"""
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
