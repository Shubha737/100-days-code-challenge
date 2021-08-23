# Day 9 Code 2
# Sum of number digits in List

total_element = int(input("Please enter the total number of elements in a list :"))
num_list = []
sum = 0

for num in range(total_element) :
        elements = int(input("Enter the element value :"))
        num_list.append(elements)
print(num_list)

for num_2 in num_list:
        sum = sum + num_2
print(sum)