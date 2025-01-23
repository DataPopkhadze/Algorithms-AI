a = 4
b = 27
c = 3

MIN = a - (a % c) + c

MAX = b - (b % c)

MAX = MAX - MIN
print((MAX / c) + 1)
