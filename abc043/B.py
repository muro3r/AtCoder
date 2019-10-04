s = input()
s_l = []

for i in range(0, len(s)):
    if s[i] == 'B' and len(s_l) > 0:
        s_l.pop()
    elif s[i] != 'B':
        s_l.append(s[i])

print(''.join(s_l))
