# for row in range(6):
#     for col in range(7):
#         if (row == 0 and col %3!=0) or (row==1 and col%3 ==0) or (row-col==2) or (row+col==8):
#             print("*", end ="")
#         else:
#             print(end="")
#     print()
    


n = 6		
for row in range(0,n):
    for col in range(0,n+1):
        if(row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print('*',end='')
        else:
            print(' ',end='')
              
    print()