#Subtract Operation1100
from timeit import default_timer as timer
import re
from collections import Counter
start= timer()
for _ in range(int(input())):
    n,k=map(int,input().split())
    res = re.findall('[-+]?\d+', input())
    a=[int(i) for i in res]
    kl=[(k+i) for i in a]
    c=Counter(a)
    s=0
    for i in kl:
        if c[i]>0:
            s=1
            break
    if s==0:
        print("no")
    else:
        print("yes")
end= timer()
print("time of execution", end-start, "sec")