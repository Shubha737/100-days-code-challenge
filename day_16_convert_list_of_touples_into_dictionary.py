# Day 16 code 1
# Convert a list of Tuples into Dictionary

list_1=[("Vijay kumar",93), ("Vikram kumar",94), ("Vivek dutta",95),
           ("Vivek kumar",96), ("Vivek choudhary",97)]
dict_1=dict()
  
for student,score in list_1:
    dict_1.setdefault(student, []).append(score)
print(dict_1)