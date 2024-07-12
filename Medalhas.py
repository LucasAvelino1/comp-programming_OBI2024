a = int(input(""))
b = int(input(""))
c = int(input(""))

if a < b and b < c and a < c:
    print("1")
    print("2")
    print("3")

elif a < b and c < b and a < c:
    print("1")
    print("3")
    print("2")

elif b < a and a < c and b<c:
    print("2")
    print("1")
    print("3")

elif b < a and c < a and b<c:
    print("2")
    print("3")
    print("1")

elif c < a and a < b and c<b:
    print("3")
    print("1")
    print("2")

elif c < a and b < a and c<b:
    print("3")
    print("2")
    print("1")