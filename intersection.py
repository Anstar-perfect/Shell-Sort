a1 = [1,3,5,7,9]
a2 = [3,5,7,11,13]

m = len(a1)
n = len(a2)

i,j=0,0

while i<m and j<n:
    if a1[i]<a2[j]:
        i+=1
    elif a1[i]>a2[j]:
        j+=1
    else:
        print(a1[i],end=' ')
        i+=1
        j+=1

