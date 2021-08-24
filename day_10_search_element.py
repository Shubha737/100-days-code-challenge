# Day 10 code 2
# Check if element exists in given list in Python

list = [10,15,20,25,30,35,40,45,50]
status = ' '

element_search = int(input("Please enter elements to search :"))

for num in list :
        diff = num -element_search
        if diff ==0 :
            status = "The element exist in the list"
            
if status == "The element exist in the list" :      
            print("Element exists")
else :
            print("Element does not exists")     
        


