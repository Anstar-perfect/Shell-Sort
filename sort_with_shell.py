n = int(input("Enter the number of elements in your array:"))
a = []
for i in range(n):
    value = int(input('Enter the integer value:'))
    a.append(value)

print('The original array:')
print(a)

interval = n//2

while interval>0:
    for i in range(interval,n):
        temp =a[i]
        j=i
        while j>=interval and a[j-interval]>temp:
            a[j] = a[j-interval]
            j-=interval

        a[j] = temp
    interval = interval//2

print('The sorted Array:')
print(a)

