inputt = str(input("Input : "))
n = len(inputt)
print("Output : ")
for i in range (n-1,-n,-1):
    for j in range (abs(i)+1):
        print (" ",end="")

    k = abs(i)+1
    l = 0
    while(k<=n):

        print(inputt[l], end = "")
        k = k+1
        l = l+1
    print()