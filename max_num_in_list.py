# to find second largest no. in a list.

num_list = [5,7,8,9,9,8]
maxi = num_list[1]
sec_maxi = num_list[0]
for i in num_list :
    if (i>maxi):
        sec_maxi = maxi
        maxi = i
    elif (i<maxi and maxi!=sec_maxi) :
        if (i>sec_maxi and sec_maxi<maxi and i!=maxi):
            sec_maxi = i

    elif (i==maxi and maxi!=sec_maxi) :
        continue
    
print(f'The Maximum is {maxi}')
print(sec_maxi)
