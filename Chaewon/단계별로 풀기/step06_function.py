#15596
# def solve(a):
#     ans = 0
#     ans = sum(a)
#     return ans
#
# a = [1,2,3,4,5]

#4673
# num_arr = list(range(1,10000))
# remove_num_arr = []
# def self_num(num) :
#     sum = 0
#
#     if int(num) < 10 :
#         sum = int(num) + int(num)
#     else :
#         sum += int(num) #값 하나 더하기
#         for i in num :
#             sum += int(i) #각 자리수 더하기
#     if sum not in remove_num_arr:
#         remove_num_arr.append(sum)
#     else : pass
#     return remove_num_arr
#
# for i in num_arr:
#     remove_num_arr = self_num(str(i))
#
# for i in range(len(remove_num_arr)):
#     if remove_num_arr[i] in num_arr :
#         num_arr.remove(remove_num_arr[i])
#
# for num in num_arr:
#     print(num)


#1065
N = int(input())
count = 0

for num in range(1,N+1):
    num = str(num)
    if len(num) < 3:
        count += 1
    elif len(num) == 3 :
        if int(num[2])-int(num[1]) == int(num[1])-int(num[0]) :
            count += 1
        else :
            pass
    else :
        pass

print(count)








#15596,4673,1065