# Day 12 code 2
# Python program to convert a given list to string

list =[]
total_element = int(input("Please enter the number of elements :"))

for num in range(total_element) :
    elements = input("Please enter the element :")
    list.append(elements)
print(list)
list_to_string = '---'.join(list)
print('Your converted list to string elements are {}'.format(list_to_string))