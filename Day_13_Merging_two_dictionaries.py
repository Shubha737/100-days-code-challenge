# Day 13 code 1
#  Merging two Dictionaries

Student_dict_1 = {'Name':'Shubham Kumar Gupta','Age':'26','Qualification':'Master In Engineering','Company':'Cognizant'}
Student_dict_2 = {'Future Ambition':'Software Developer','Method':'Python and DSA learning'} 

# to merge two different dictionary, i have used .update() pre-defined function. 
# Earlier, i thought to solve this problem using .union(), but it works with list and tuples only.

(Student_dict_1.update(Student_dict_2))

print('The merged dictionary looks like {}'.format(Student_dict_1))



 