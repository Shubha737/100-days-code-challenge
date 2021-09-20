# to find largest no. in a list.

num_list = [55,54,75,3,90,56,1,9054,0,98]
maxi = num_list[1]
for i in num_list :
    if (i>=maxi):
        maxi = i
    else :
        continue
    
print(f'The Maximum is {maxi}')
