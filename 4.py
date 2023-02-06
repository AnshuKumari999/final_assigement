# 4. Reverse the list by using negative index and apply logic also.
print("\n")
# reverse list using negative index
original_list = [1,2,3,4,5,7,8,9,15,18]
reversed_list = original_list[::-1]
print(reversed_list)

# reverse list using for loop
for ele in original_list:
    reversed_list = [ele] + reversed_list
print(reversed_list)
