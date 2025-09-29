#Print the patterns
"""
*
**
***
****
*****
"""
for i in range(6):
    for j in range(i):
        print("*",end='')
    print("")

"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
#upper part
k = 1
for i in range(4, 0, -1):
    for j in range(i):
        print(" ", end="")
    print("*"*k,end="")
    for j in range(i):
        print(" ",end="")
    k=k+2    
    print()
#lower part  
for i in range(0,5):
    for j in range(i):
        print(" ",end="")
    print("*"*k,end="")
    for j in range(i):
        print(" ",end="")
    k=k-2    
    print()
