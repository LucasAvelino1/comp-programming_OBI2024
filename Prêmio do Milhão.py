n = int(input(""))
pn = n
s = 0

while n != 0:
    t = int(input(""))
    s = s + t
    n = n-1

    if s >= 1000000:
        break

print(pn-n)