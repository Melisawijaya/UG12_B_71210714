n = int(input("Input : "))

i = n-1

while(i>0):
    for j in range (abs(i)):
        print (" ",end=" ")
    print("*", end=" ")

    if(i==n-1):
        i=n-1
    else:
        k = 0
        m = n
        while(i<m):
            if(i==m-2):
                print("*", end= " ")
            else:
                print(" ", end=" ")
            k = k+1
            m = m-1
    i = i-1
    print()

if(n==0):
    print(" ")
else:
    for l in range (abs(n)):
        print("*", end=" ") 