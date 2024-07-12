n = int(input(""))
p, c, q = input("").split()
p, q = map (int, [p, q])

if c == "+":
    if p+q <= n:
        print("OK")
    else:
        print("OVERFLOW")

if c == "*":
    if p*q <= n:
        print("OK")
    else:
        print("OVERFLOW")