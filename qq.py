z = str(input())
q = [int(s) for s in z.split() if s.isdigit()]
print(q)
qq = []
for i in range(len(q)):
    qq.append(q[i] % 10)
print(qq)
qw = []
for i in range(z):
    if '1234567890'.find(i) != -1:
        qw.append(int(i))
print(qw)
qqq = [0] * 10000
for i in range(len(qq)):
    qqq[qq[i]] = qqq[i] + 1

for i in range(len(qw)):
    if qqq[qw[i]] == 0:
        qqq[qw[i]] = -1
print("{", end="")
for i in range(len(qqq)):
    if qqq != 0:
        if qqq[i] == -1:
            print('"', end="")
            print(i, end="")
            print('"', end=" ")
            print(':', 0, end="")
        else:
            print('"', end="")
            print(i, end="")
            print('"', end="")
            print(':', qqq[i], end="")
    for q in range(len(qqq)):
        if qqq[q] != 0 and q > i:
            print(",", end=" ")
            break
    if i == len(qq) - 1:
        print("}")
        break
