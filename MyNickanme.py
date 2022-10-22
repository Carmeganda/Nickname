#Assignment 1:
#Create a program that will print your nickname using only asterisk character (*)

from unicodedata import name


name = "ELA"
print_E = [["" for i in range (7)] for j in range(5)]
print_L = [["" for i in range (7)] for j in range(5)]
print_A = [["" for i in range (7)] for j in range(5)]

#Code for E
for row in range(5):
    for colum in range(5):
        if (colum==0 or (row==0 or row==2 or row==4) and (colum>0)):
            print("*",end="")
        else:
            print(end=" ")
    print()
         
#Code for L
for row in range(7) :
    for col in range(5) :
        if col==0 or (row==6 and col>0) :
            print("*",end=" ")
        else:
            print(end=" ")
    print()

#Code for A
str1 = " "
for row in range(7) :
    for col in range(5) :
        if (col==0 or col==4) or ((row==0 or row==3) and (col>0 and col<4)) :
            str1 = str1+"*"
        else: 
            str1 = str1+" "
    str1 = str1+"\n"
print(str1)


for i in range(7) :
    for j in range(5) :
        print(print_E[i][j],end="")
    print (end=" ")
    for j in range(5) :
        print (print_L[i][j],end="")
    print (end=" ")
    for j in range(5) :
        print (print_A[i][j],end="")
    print (end=" ")
    print()

