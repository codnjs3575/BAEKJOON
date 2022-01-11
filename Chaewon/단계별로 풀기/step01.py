#10718
for i in range(2):
    print("강한친구 대한육군")

#1000
a,b= map(int,input().split())
print(a+b)

#1001
a,b= map(int,input().split())
print(a-b)

#10998
a,b= map(int,input().split())
print(a*b)

#1008
a,b= map(int,input().split())
print(a/b)

#10869
a,b= map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print('%d' % (a/b) )
print(a%b)

#10430
첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C,
셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
a,b,c= map(int,input().split())
print('%d' % ((a+b)%c))
print('%d' % int( ( (a%c) + (b%c) ) % c ) )
print('%d' % ((a*b)%c))
print('%d' % int( ( (a%c) * (b%c) ) % c ) )

#2588
num1 = int(input())
num2 = int(input())

print(num1 * (num2 % 10))
print(num1 * ((num2//10) % 10))
print(num1 * (num2//100))
print(num1 * num2)






