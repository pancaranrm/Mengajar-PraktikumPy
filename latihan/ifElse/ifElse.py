"""
 Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
    Unit                                                     Price  
First 100 units                                             no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)
"""

amt = 0
calculate = int(input("Input from 100-350 "))
if calculate <= 100:
   amt = 0
if calculate > 100 and calculate <= 200:
    amt =(calculate-100)*5
if calculate >200:
    amt = 500 +(calculate-200)*10
print("Amount to pay:",amt)





