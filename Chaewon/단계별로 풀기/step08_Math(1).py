# 1712
A, B, C = map(int,input().split())

count = 1

if B >= C:
    print('-1')
else :
    print((A // (C-B)) + 1)

# 2292
N = int(input())

count = 0
min_no = 2
max_no = 7

if N == 1 :
    print(1)
elif N <= 7 :
    print(2)
else :
    while True :
        min_no = min_no + (6*count)
        max_no = min_no + (6*(count+1)) -1
        count += 1
        if (min_no + (6*count)) <= N <= (max_no + (6*(count+1))) :
            break
    print(count+2)

# 1193
import sys
N = int(sys.stdin.readline())

a = 1 # 분자
b = 1 # 분모
c = a+b

if N == 1 :
    print("%d/%d"% (a,b))
elif N == 2 :
    print("%d/%d" % (a, b + 1))
elif N == 3:
    print("%d/%d" % (a + 1, b))
else :
    pass

