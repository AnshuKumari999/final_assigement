# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).

l = [i for i in range( 2000 , 3200) 
if i % 7 == 0 if i % 5 != 0] 
print(l)
