#Boxes And Balls2300
from timeit import default_timer as timer
start= timer()
n = int(input())
colors = list(map(int, input().strip().split()))

if n % 2 == 0:
    colors.append(0)

import heapq

heapq.heapify(colors)
penalty = 0

while (len(colors) > 2):
    a = heapq.heappop(colors)
    b = heapq.heappop(colors)
    c = heapq.heappop(colors)
    penalty += (a + b + c)

    heapq.heappush(colors, a + b + c)

print(penalty)
end = timer()
print("time of execution", end-start, "sec")