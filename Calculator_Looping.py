x=0
while(x<=5):
  A=int(input("Enter A value:"))
  B=int(input("Enter B value:"))
  C=int(input("1.add 2.sub 3.mul 4.div 5.exit: "))
  if(C==1):
    print(A+B)
  elif (C==2):  
    print(A-B)
  elif (C==3):  
    print(A*B)
  elif (C==4):
    print(A/B)
  elif (C==5):
    print("Exit successfully")
    x=5
  else:  
    print("enter valid option")
  x+=1
  
#Output:
Enter A value:12
Enter B value:65
1.add 2.sub 3.mul 4.div 5.exit: 2
-53
Enter A value:55
Enter B value:65
1.add 2.sub 3.mul 4.div 5.exit: 5
Exit successfully
