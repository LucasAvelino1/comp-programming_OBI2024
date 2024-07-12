n, k = map(int, input("").split())
a = list(map(int, input("").split()))

sumt = []
sumtpf = []
app = []
sum = 0

for x in a:
    for y in a:
        if x <= y:
            sum = sum + 1
    if sum == k:
        sumtpf.append(x)
        app.append(sum)
    elif sum >= k:
        sumt.append(x)
        app.append(sum)

    sum = 0

#print(sumt)



if len(sumtpf) != 0:
    print(min(sumtpf))

else:
    index_minapp = app.index(min(app))
    index_minsumt = sumt.index(sumt[index_minapp])
    minsumt = sumt[index_minsumt]
    print(minsumt)
