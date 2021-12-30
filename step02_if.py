#1330
# A,B = map(int,input().split())
#
# if A > B :
#     print('>')
# elif A == B:
#     print('==')
# else :
#     print('<')

#9498
# score = int(input())
#
# if score >= 90 :
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else :
#     print("F")

#2753
# year = int(input())
#
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print(1)
# else :
#     print(0)

#14681
# num1 = int(input())
# num2 = int(input())
#
# if (num1>0 and num2>0):
#     print(1)
# elif (num1<0 and num2>0):
#     print(2)
# elif (num1<0 and num2<0):
#     print(3)
# else : print(4)

#2884
H,M = map(int,input().split())

M -= 45

if M < 0 :
    M += 60
    H -= 1
    if H == -1 :
        H = 23

print(H,M)

