from random import randint


def random_with_n_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n) - 1
    return randint(range_start, range_end)


def main():
    for mciNumbers in range(0, 100):
        print(random_with_n_digits(9))


if __name__ == '__main__':
    main()
