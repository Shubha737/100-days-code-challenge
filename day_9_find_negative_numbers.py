# Day 9 code 1
# Python program to print negative numbers in a list

total_element = int(input("Enter the total no. of elements in the list :"))

list =[]

for num in range (total_element) :

    listss= int(input("Please enter the list value:"))
    final_list = list.append(listss)

print(list) 

for ele in list :   
    if ele < 0 :
        print (ele)