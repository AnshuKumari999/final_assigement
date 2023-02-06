# Create a list by picking an odd-index items from the first list and even index items from the second return third list.
l1, l2, l3 = [17,19,21,23,9,7], [2,1,5,6,4,22], []
o= l1[1::2]
print("Printing the odd indexing element from list-1 : ")
print(o)
e = l2[0::2]
print("Printing the even indexing element from list-2 : ")
print(e)
print("Printing a third list with the help of list-1 and list-2")
l3.extend(o)
l3.extend(e)
print(l3)