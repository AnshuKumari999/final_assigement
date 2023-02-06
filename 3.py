
# 3.convert a number into binary and binary to number.

# Binary to Decimal
n = input("Enter a Binary Number : ") 
l = list(n)
sum = 0
l.reverse()
for i in range (len(l)):
    sum = sum + int(l[i])*2**i
print(sum)

# Decimal to Binary

n = int(input("Enter a Number : "))
l = list()
while n!=0:
    r=n%2
    l.append(r)
    n=n//2
l.reverse()
for a in l:
    print(a,end = "")
