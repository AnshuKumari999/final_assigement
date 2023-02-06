#Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list by using list comprehension 
#dict ={"key1":1234, "k2":"ram"}
#list= [1234,"ram"]

dict={"key1":1234,"k2":"ram"}
list=[1234,"rhain", "ram", 5678]
l=[]
for key,value in dict.items():
    for a in list:
        if(value == a):
            l.append(a)
print("Print the list and dict common values",l)

