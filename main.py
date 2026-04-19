a = [3,2,4,13,12,98,56]

n = len(a)

interval = n//2

while interval>0:
    for i in range(interval,n):
        temp = a[i]
        j=i
        while j >= interval and a[j-interval]>temp:
           a[j] = a[j-interval]
           j-=interval

        a[j]=temp
    interval //=2

print('Sorted Array:')
print(a)