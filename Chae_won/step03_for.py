#2739
# num = int(input())
#
# for i in range(1,10):
#     print(f'{num} * {i} = {num * i} ')

#10950
# rpt_no = int(input())
#
# for i in range(rpt_no):
#     num1,num2 = map(int,input().split())
#     print(num1+num2)

#8393
# n = int(input())
#
# sum = 0
# for i in range(n,0,-1):
#     sum += i
# print(sum)

#15552
# n = int(input())
# import sys
# for i in range(n):
#     A,B = map(int,sys.stdin.readline().rstrip().split())
#     print(A+B)

#2741
# n = int(input())
#
# for i in range(1,n+1):
#     print(i)

#2742
# n = int(input())
# for i in range(n,0,-1):
#     print(i)

#11021
# n = int(input())
# import sys
# for i in range(1,n+1):
#     A,B = map(int,sys.stdin.readline().rstrip().split())
#     print(f'Case #{i}: {A} + {B} = {A + B}')

#2438
# n = int(input())
# for i in range(1,n+1):
#     print('*'*i)

#2439
# n = int(input())
# for i in range(1,n+1):
#     print(' '*(n-i),'*'*i,sep='')

N, X = map(int,input().split())

num_arr = list(map(int,input().split()))
if len(num_arr) == N:
    for i in range(N):
        if num_arr[i] < X:
            print(num_arr[i],end=" ")


# 10430,2588,1330,9498,2753,14681,2884,2739,
# 10950,8393,15552,2741,2742,11021,2438,2439,
