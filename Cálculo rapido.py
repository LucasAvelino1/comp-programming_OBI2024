s = int(input(""))
a = int(input(""))
b = int(input(""))

i = a
counter = 0
sum = 0

while i <= b:
    sum = 0
    i_arr = list(str(i))
    for c in i_arr:
        c = int(c)
        sum = sum + c

    if sum == s:
        counter = counter + 1

    i = i + 1

print(counter)