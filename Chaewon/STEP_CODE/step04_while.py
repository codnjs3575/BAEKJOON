# 10430,2588,1330,9498,2753,14681,2884,2739,
# 10950,8393,15552,2741,2742,11021,2438,2439,
# 10952,1110

#10952
# import sys
# while True :
#     try :
#         a = sys.stdin.readline()
#         c, d = map(int, a.split())
#         print(c+d)
#     except :
#         break

#1110
N = input() #변경 x, 초기값 비교용
count = 0
new_N = N #변경 ver

while True:
    if len(new_N) < 2:
        new_N = new_N+new_N
        N = N+N
    sum = int(new_N[0])+int(new_N[1])
    if sum >= 10:
        sum = str(sum)[1]

    new_N = new_N[1]+str(sum)

    count += 1

    if new_N == N :
        print(count)
        break

