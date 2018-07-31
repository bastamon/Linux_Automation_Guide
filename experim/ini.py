import sys


def main():
    sys.argv.append("")
    la = sys.argv[1]
    huiwen(la)


def huiwen(n):
    tmp = n
    sum = 0
    while (n):
        sum = sum * 10 + n % 10
        n /= 10

    if tmp == sum:
        return 1
    else:
        return 0


if __name__ == "__main__":
    main()
