x = int(input("введите число: x"))
y = int(input("введите число: y"))
n = int(input("введите число: n"))
for i in range(1,n+1,1):
    x = x+ (y*x)/100
print(x)