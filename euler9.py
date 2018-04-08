def triplet_product(triplet_sum):
    for a in range(triplet_sum // 2, 0, -1):
        for b in range(a, 0, -1):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and a+b+c == triplet_sum:
                return int(a*b*c)
    return -1

if __name__ == '__main__':
    print(triplet_product(1000))