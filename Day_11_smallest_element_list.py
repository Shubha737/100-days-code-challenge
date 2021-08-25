# Day 11 code 2
# Python program to find smallest number in a list

total_element = int(input("Enter the total number of elements :"))
list = []

for num in range(total_element):
        elements = float(input("Enter the element value:"))
        list.append(elements)
print(list)

# will use the min() function to find the minimum element of the list.

minimum_element = min(list)
print(minimum_element)
