from sys import stdin

def min_refills(distance, tank, stops):
    # Add the starting point (0) and destination (distance) to the list of stops
    stops = [0] + stops + [distance]
    num_refills = 0
    current_pos = 0  # Index of the current stop

    while current_pos < len(stops) - 1:
        last_pos = current_pos

        # Move as far as possible within the tank's capacity
        while current_pos < len(stops) - 1 and (stops[current_pos + 1] - stops[last_pos] <= tank):
            current_pos += 1

        if current_pos == last_pos:
            # Can't reach the next stop from the current position
            return -1

        if current_pos < len(stops) - 1:
            # Refueling needed if we haven't reached the destination yet
            num_refills += 1

    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
