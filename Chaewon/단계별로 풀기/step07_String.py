# 11654
in_msg = input()
print(ord(in_msg))

# 11720
N = int(input())
num_arr = input()

if len(num_arr)==N :
    sum = 0
    for i in num_arr:
        sum += int(i)
print(sum)

# 10809
S = input()
num = []

for _ in range(26):
    num.append(-1)

for i in range(len(S)):
    if num[ord(S[i])-97] >= 0:
        pass
    else: num[ord(S[i])-97] = i

for n in num:
    print(n,end=" ")

# 2675
T = int(input())
out_msg = []

for i in range(T):
    a = ""
    msg = []
    S = input().split(" ")

    rp_no = int(S[0])
    str = S[1]

    for i in range(len(str)):
        msg.append(str[i] * rp_no)
    a = "".join(msg)
    out_msg.append(a)

for m in out_msg:
    print(m)

#1157
in_msg = input().upper()

cnt = [0] * 26
for msg in in_msg:
    cnt[ord(msg)-ord('A')] += 1

if cnt.count(max(cnt)) > 1 :
    print("?")
else :
    alpha = cnt.index(max(cnt))
    print(chr(alpha+ord('A')))

# 1152
in_msg = input().split(" ")
count = 0
for msg in in_msg:
    if not msg.isalpha():
        count += 1

print(len(in_msg)-count)

# 2908
num_arr = input().split()
num = []

for i in range(2):
    num.append(num_arr[i][::-1])
print(max(num))

# 5622
in_msg = input()
sum = 0
for msg in in_msg:
    n = ord(msg) - ord("A")
    if n <= 2:
        sum += 3
    elif n <= 5:
        sum += 4
    elif n <= 8:
        sum += 5
    elif n <= 11:
        sum += 6
    elif n <= 14:
        sum += 7
    elif n <= 18:
        sum += 8
    elif n <= 21:
        sum += 9
    else:
        sum += 10
print(sum)

# 2941
in_msg = input()
alpha = ["c=",'c-','dz=','d-','lj','nj','s=','z=']
count = 0
msg = in_msg[0:2]

while True :
    if in_msg[0:2] in alpha:
        count += 1
        in_msg = in_msg[2:len(in_msg)]
        msg = in_msg[0:2]
    elif in_msg[0:3] in alpha:
        count += 1
        in_msg = in_msg[3:len(in_msg)]
        msg = in_msg[0:2]
    else :
        count += 1
        in_msg = in_msg[1:len(in_msg)]
        msg = in_msg[0:2]

    if len(in_msg) == 0 :
        break

print(count)

# 1316
N = int(input())
all_count = 0
for _ in range(N):
    msg = input()
    count_i = len(msg)

    msg_set = sorted(list(set(msg))) # 알파벳 중복없이 정렬하여 저장

    for i in range(len(msg_set)) :
        m_i = msg_set[i]
        count = msg.count(m_i)

        if count > 1:
            idx = msg.index(m_i) # 시작 위치
            last_idx = idx + count #끝 위치
            msg_str = msg[idx:last_idx]
            msg_str_cnt = msg_str.count(m_i)
            if msg_str.count(m_i) != count:
                count_i -= 1

    if count_i == len(msg):
        all_count += 1

print(all_count)


