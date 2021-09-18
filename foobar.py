# Day 35/100
# Problem statement :- Write a function called FooBar that takes input integer n and prints all the numbers from 1 upto n in a new line. If the number is divisible by 3 then print "Foo", if the number is divisible by 5 then print "Bar" and if the number is divisible by both 3 and 5, print "FooBar". Otherwise just print the number. 

def foobar(num):

    for n in range(1,num+1):
        if (n%3 ==0 and n%5==0):
            print('FooBar')
        elif (n%3 ==0):
            print('Foo')
        elif (n%5==0):
            print('Bar')
        else :
            print(n)


foobar(15)
