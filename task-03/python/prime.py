n=int(input('Enter n: '))
for i in range(2,n+1):
    for s in range(2,n+1):
        if i%s==0:
            break
    if i==s:
        print(i,)
