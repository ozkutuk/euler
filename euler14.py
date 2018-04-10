def count_collatz_steps(n, pre_calc):
    steps = 1
    init_n = n
    while(n > 1):
        if n in pre_calc:
            steps += pre_calc[n] - 1
            break
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        steps += 1
    pre_calc[init_n] = steps
    return steps

def validate_collatz(n):
    while(n > 1):
        print(n, end=' -> ')
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
    print(1)

def longest_collatz(upper_limit):
    longest = 1
    length = 0
    pre_calc = dict()
    for n in range(1, upper_limit):
        current_length = count_collatz_steps(n, pre_calc)
        if current_length > length:
            longest = n
            length = current_length
    return longest

if __name__ == '__main__':
    res = longest_collatz(1000000)
    print(res)
