def change(money):
    count_10 = 0
    count_5 = 0
    count_1 = 0

    while money != 0:
        if money >= 10:
            money -= 10
            count_10 += 1
        elif money >= 5:
            money -= 5
            count_5 += 1
        else:
            money -= 1
            count_1 += 1

    """    parts = []
    parts.extend(["10"] * count_10)
    parts.extend(["5"] * count_5)
    parts.extend(["1"] * count_1)"""

    return ((count_1) + (count_10) + (count_5))


if __name__ == '__main__':
    m = int(input())
    print(change(m))
