"""
Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
    
        Cost price (in Rs)                                       Tax
        > 100000                                                  15 %
        > 50000 and <= 100000                          10%
        <= 50000                                                  5%

"""
from re import I


t = 0
i = int(input("Input your bike price"))
if i > 100000:
    t = 15/100*i 
elif i > 50000 and i <= 100000 :
    t = 10/100*i 
else:
    t = 5/100*i 
print("Your tax is...",t)
 

