def longest_collatz_sequence(n):
    length = 2
    current = 2
    while current < n or (current-1) % 3 == 0:
        # if (current-1) % 3 == 0:
        #     current = current / 3
        print(current)
        next = (current-1) / 3
        if next != 0 and next != 1 and ((next-1) % 3 != 2 and not next % 2 == 0) and next.is_integer():
            current = int(next)
        else:
            current *= 2
        length += 1
    return current // 2

def validate_collatz(n):
    while(n > 1):
        print(n, end=' -> ')
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
    print(1)
if __name__ == '__main__':
    res = longest_collatz_sequence(1000000)
    validate_collatz(res)