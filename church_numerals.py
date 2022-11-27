
def zero(f, x):
    return x


def one(f, x):
    return f(x)


def two(f, x):
    return f(f(x))


def three(f, x):
    return f(f(f(x)))


def to_int(f):
    return f(lambda x : x + 1, 0)


class numbers:
    ZERO = zero
    ONE = one
    TWO = two
    THREE = three


def length(l, acc):
    if l == []:
        return acc
    return length(l[1:], acc + 1)

length([1, 2, 3, 4, 5], 0)


if __name__ == "__main__":
    print("This is number", to_int(numbers.ZERO))
    print("This is number", to_int(numbers.ONE))
    print("This is number", to_int(numbers.TWO))
    print("This is number", to_int(numbers.THREE))
