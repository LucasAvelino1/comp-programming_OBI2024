m = int(input(""))
a = int(input(""))
b = int(input(""))

c = m - a - b

if c > a and c > b:
     print(c)

elif a > c and a > b:
    print(a)

else:
    print(b)