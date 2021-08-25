# Day 11 code 1
# Reversing a List in Python

total_element = int(input("Enter the total number of elements :"))
list = []
rev_list = []

for num in range(total_element):
        elements = (input("Enter the element value:"))
        list.append(elements)
print(list)

list.reverse()
print(list)



