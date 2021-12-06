# ------28.11.21--------#
# 2
'''
print('x y z w F')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                F = not(x == (not y)) or ((x and w) == (z and not w))
                if F == 0:
                    print(x, y, z, w, F)
'''

# 5
'''
def F(N):
    N = str(N)
    N = N.replace('', ' ').split()
    N = [int(i) for i in N]
    res1 = 0
    res2 = 0
    for dig in range(0, len(N)):
        digit = N[dig]
        if digit % 2 == 0:
            res1 += digit
        if dig % 2 != 0:
            res2 += digit
    R = abs(res2 - res1)
    return R


for i in range(2, 10000):
    if F(i) == 13:
        print(i, F(i))
        break
'''

# 6
'''
counter = 0
for s in range(1, 10000):
    s1 = s
    s = 3 * (s // 10)
    n = 1
    while s < 221:
        s += 13
        n *= 2
    if n == 128:
        counter+=1
        print(s1, n, counter)
'''

# 7
'''
v = 160 * 1024 * 8
size = 256 * 640
res = v/size
print(res)
'''

# 8
'''
alphabet = ['А', 'В', 'Т', 'О', 'Р']
alphabet = sorted(alphabet)
count = 0
for A in alphabet:
    for B in alphabet:
        for C in alphabet:
            for D in alphabet:
                res = A + B + C + D
                count += 1
                if res == 'ВАТА':
                    print(count, res)
'''

# 12
'''
def F(n):
    n = str(n)
    while '111' in n or '222' in n:
        n = n.replace('111', '22', 1)
        n = n.replace('222', '1', 1)
    return n


for i in range(200, 10000):
    stri = '1' * i
    if F(stri).count('1') == len(F(stri)):
        print(i)
        break
'''

# 14

'''num = 4 ** 36 + 3 * 4 ** 20 + 4 ** 15 + 2 * (4 ** 7) + 49
res = ''
while num > 0:
    ost = num % 16
    num = num // 16
    res += str(ost) + ' '
print(res[::-1])
'''

# 16
'''
def F(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return F(n / 2)
    elif n > 0 and n % 2 != 0:
        return 1 + F(n - 1)

count = 0
for i in range(1, 500 + 1):
    if F(i) == 8:
        count+=1
        print(i, count)
'''

# 17

'''
f = open('C:/Users/Alex/Downloads/17 (1).txt', 'r').read()
f = f.split('\n')
del f[-1]
f = [int(i) for i in f]
count = 0
maxi = 0
for i in range(0, len(f) - 1):
    if f[i] % 3 == 0 or f[i + 1] % 3 == 0 and f[i] + f[i + 1] % 5 == 0:
        count += 1
        maxi = max(maxi, f[i] + f[i + 1])
        print(count, f[i], f[i + 1], maxi)
'''

# 22
'''
for x in range(5, 1000):
    x1 = x
    a = 7 * x + 27
    b = 7 * x - 33
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 15:
        print(x1, a)
        break
'''

# 23
'''
def F(curr, end):
    if curr == end: return 1
    if curr > end: return 0
    if curr <= end:
        R = F(curr + 1, end) + F(curr * 3, end)
        return R


print(F(2, 28) * F(28, 90))
'''

# 24
'''
file = open('C:/Users/Alex/Downloads/24.txt').read().replace('', ' ').split()
counter = 0
counter_A = 0
maxi = 0
for letter in file:
    if letter == 'A':
        counter_A += 1
    if letter != 'A':
        counter += 1
    if counter_A == 2:
        maxi = max(maxi, counter)
        counter_A = 0
        counter = 0
print(maxi)
'''

# 25

'''
def M(N):
    counter_div = 0
    arr_div = []
    for div in range(2, round(N ** 0.5) + 1):
        div2 = N / div
        if N % div == 0:
            arr_div.append(div)
        if N % div2 == 0:
            arr_div.append(div2)
    if len(arr_div) < 5:
        return 0
    elif len(arr_div) >= 5:
        arr_div = sorted(arr_div)
        arr_div = [arr_div[i] for i in range(0, 4 + 1)]
        result = 1
        for num in arr_div:
            result *= num
        return result


counter = 0
for n in range(200000000, 210000000 + 1):
    if 0 < M(n) < n:
        counter += 1
        print(n, M(n))
    if counter == 6: break
'''

# ------06.12.2021-------#
# 2

'''print('x y z w F')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                F = not (not z == y) or ((w and not x) == (y and x))
                if F == 0:
                    print(x, y, z, w, F)'''

# 5
'''
def F(N):
    N = str(N)
    s1 = 0
    s2 = 0
    for i in range(len(N)):
        if int(N[i]) % 2 == 0:
            s1 += int(N[i])
        elif i % 2 != 0:
            s2 += int(N[i])
    R = abs(s1 - s2)
    return R


for num in range(2, 1000):
    if F(num) == 11:
        print(num)
        break'''

# 6
'''
counter = 0
for s in range(1, 20000):
    s1 = s
    s = 3 * (s // 10)
    n = 1
    while s < 221:
        s = s + 13
        n = n * 2
    if n == 256:
        counter += 1
        print(n,s1, counter)
'''

# 7
'''v = 640 * 1024 * 8
s = 512 * 640
print(2**(v/s))'''

# 8
'''
arr = ['А', 'В', 'Т', 'О', 'Р']
arr = sorted(arr)
count = 0
for A in arr:
    for B in arr:
        for C in arr:
            for D in arr:
                count += 1
                R = A + B + C + D
                if R == 'ТАРА':
                    print(count, R)
                    break
'''

# 12
'''
def F(st):
    st = str(st)
    while '111' in st or '222' in st:
        st = st.replace('111', '22', 1)
        st = st.replace('222', '1', 1)
    return st


for i in range(200, 10000):
    stri = '1' * i
    if F(stri).count('1') == 0:
        print(i, F(stri))
        break
'''

# 14
'''
r = 4 ** 34 + 5 * (4 ** 22) + 4 ** 13 + 2 * (4 ** 9) + 82

res = ''
while r > 0:
    ost = r % 16
    r = r // 16
    res += ' '+str(ost)
print(res[::-1])'''

# 16
'''
def F(n):
    if n == 0: return 0
    if n > 0 and n % 2 == 0: return F(n / 2)
    if n % 2 != 0: return 1 + F(n - 1)


count = 0
for i in range(1, 900 + 1):
    if F(i) == 9:
        count += 1
print(count)'''

# 17
'''
f = open('C:/Users/Alex/Downloads/17 (2).txt', 'r').read()
f = f.split('\n')
del f[-1]
f = [int(i) for i in f]
count = 0
max_s = 0
for i in range(len(f)-1):
    if f[i] % 5 == 0 or f[i + 1] % 5 == 0 and f[i] + f[i + 1] % 7 == 0:
        count += 1
        max_s = max(max_s, f[i] + f[i + 1])

print(count, max_s)'''

# 22
'''
for x in range(10, 10000):
    a = 7 * x + 27
    b = 7 * x - 33
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 10:
        print(x, a)
        break'''

#23
'''
def F(curr, end):
    if curr == end: return 1
    if curr > end: return 0
    if curr <= end:
        R = F(curr + 1, end) + F(curr * 3, end)
        return R


print(F(2, 26) * F(26, 87))
'''

