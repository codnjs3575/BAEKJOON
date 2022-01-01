#10818
# N = int(input())
#
# num_arr = list(map(int,input().split()))
#
# if len(num_arr) == N :
#     print(min(num_arr),max(num_arr))


#2562
# num_arr = list()
# count = 0
# max_num = 0
#
# for i in range(9):
#     num = int(input())
#     num_arr.append(num)
#     if num > max_num :
#         max_num = num
#         count = i+1
#
# print(max_num)
# print(count)

#2577
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# count = 0
# count_arr = []
#
# for j in range(10): #0
#     count = 0
#     for i in str(num1 * num2 * num3): #11100022
#         if int(i) == j :
#             count += 1
#     count_arr.append(count)
#
# for k in range(10):
#     print(count_arr[k])

#3052
# num_arr = []
# a_arr = []
#
# count = 0
#
# for i in range(10):
#     num = int(input())
#     num_arr.append(num)
#     if len(a_arr) == 0:
#         a_arr.append(num % 42) #[1]
#     else : #[1]
#         for j in range(len(a_arr)):
#             if num % 42 == a_arr[j]:
#                 pass
#             else :
#                 count += 1
#         if count == len(a_arr):
#             a_arr.append(num % 42)  # [1]
#         count = 0
#
# print(len(a_arr))

#1546
# N = int(input())
#
# num_arr = list(map(int,input().split()))
# num_arr2 = []
# sum = 0
# if  len(num_arr) != N : pass
# else :
#     M = max(num_arr)
#     for i in range(N):
#         sum += num_arr[i]/M*100
# print(sum/N)

# N = int(input())
# str_arr = []
# for i in range(N):
#     str_arr.append(input())
#
# count = 0
# sum_arr = []
# sum = 0
#
# for str in str_arr:
#     for j in range(len(str)):
#         if (str[j] == "O" and j == 0)  or (str[j] == "O" and count == 0):
#             count = 1
#         elif str[j] == "O" and j > 0:
#             if str[j-1] == "O" :
#                 count += 1
#             else :
#                 count = 1
#         else :
#             count = 0
#         sum += count
#     sum_arr.append(sum)
#     sum = 0
#
# for i in range(N):
#     print(sum_arr[i])

#4344
C = int(input())
all_score_arr = []
avg_arr = []

for c in range(C):
    all_score_arr.append(list(map(int, input().split())))


for array in all_score_arr:
    sum = 0
    count = 0
    N = array[0]
    score_arr = array[1:]

    for i in range(N):
        sum += score_arr[i]
    avg = sum / len(score_arr)
    for j in range(N):
        if score_arr[j] > avg:
            count += 1

    avg_arr.append(count/len(score_arr) * 100)

for k in range(C):
    print( '%.3f%%' % avg_arr[k])

# 10818,2562,2577,3052,1546,4344

