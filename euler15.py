from functools import lru_cache

@lru_cache(maxsize=500)
def countPaths(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return 1
    return countPaths(x - 1, y) + countPaths(x, y - 1)


if __name__ == '__main__':
    print(countPaths(20, 20))

