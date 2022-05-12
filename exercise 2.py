#sumofcubes1100
from timeit import default_timer as timer
start= timer()
t = int(input())
def cr(n):
    return round(n ** (1 / 3))
def q(n):
    for i in range(1, cr(n) + 10):
        a = i ** 3
        if a < n:
            b = cr(n - a)
            if (a + (b ** 3)) == n:
                return "YES"
        else:
            return "NO"
    return "NO"
for i in range(t):
    n = int(input())
    print(q(n))
end= timer()
print("time of execution", end-start, "sec")