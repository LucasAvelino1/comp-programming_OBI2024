h = int(input(""))
m = int(input(""))
s = int(input(""))
t = int(input(""))

qh = 0
qm = 0
qs = 0

while t > 3600:
    qh = qh + 1
    t = t - 3600

while t >= 60:
    qm = qm + 1
    t = t - 60

qs = t

h = h + qh
m = m + qm
s = s + qs

qh = 0
qm = 0
qs = 0

while s >= 60:
        s = s - 60
        qm = qm + 1

m = m + qm

while m >= 60:
        m = m - 60
        qh = qh + 1

h = h + qh

while h >= 24:
    h = h - 24

print(h)
print(m)
print(s)