# Day 10 code 1
# Python program to find Cumulative sum of a list

total_element = int(input("Enter the total number of elements :"))
list = []
cum_list = []
sum =0

for num in range(total_element):
        elements = int(input("Enter the element value:"))
        list.append(elements)
print(list)

for numb in list :
        print(numb)
        sum = sum + numb
        cum_list.append(sum)
         
print(cum_list)