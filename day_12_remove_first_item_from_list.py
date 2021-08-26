# Day 12 code 1
# Write a Python program to remove the first item from a list

total_element = int(input("Enter the total number of elements :"))
list = []

for num in range(total_element):
        elements = input("Enter the element value:")
        list.append(elements)
print(list)

# to remove the first item of the list, i have used .remove() function 
list.remove(list[0])
print('The new formatted list is {}'.format (list))

# Fun and knowledgable facts
# Initially, i was not able to remove the first item using pre-defined function. But, list[] i.e. square parenthesis gives the flexibility to put index no. in it, so that pre-defined function operate at that particular index only. 