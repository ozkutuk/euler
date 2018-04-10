from itertools import count

def nth_triangle(n):
    return n * (n+1) // 2

def next_triangle():
    for n in count(1):
        yield nth_triangle(n)
    
def count_divisors(number):
    divisor_test = [1] * int(number ** 0.5)
    divisor_count = 0
    i = 0
    while i < len(divisor_test):
        if divisor_test[i] == 1:
            # test divisibility by i+1 (0th index corresponds to 1 and so on)
            divisor = i + 1
            if number % divisor == 0:
                divisor_count += 2
            else:
                for non_divisor in range(divisor, len(divisor_test), divisor):
                    divisor_test[non_divisor - 1] = 0
        i += 1
    return divisor_count + 1

def triangle_over_x_divisors(x):
    for triangle in next_triangle():
        a = count_divisors(triangle)
        if a > x:
            return triangle

if __name__ == '__main__':
    print(triangle_over_x_divisors(500))
