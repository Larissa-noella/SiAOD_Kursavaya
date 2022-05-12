#Poisoned Dagger1200
from timeit import default_timer as timer
start= timer()
tests = int(input())
for _ in range(tests):
    [n, h] = [int(x) for x in input().split()]
    attacks = [int(x) for x in input().split()]
    d = sorted(a2 - a1 for a1, a2 in zip(attacks, attacks[1:]))
    s = 0

    for k in d:
        if k > ((h - s) // n):
            break

        s += k
        n -= 1
    print(0 - (s - h) // n)
end= timer()
print("time of execution", end-start,"sec")