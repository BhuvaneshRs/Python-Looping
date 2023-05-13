Alpha=input("are you ready in looping y/n :")
while(Alpha=="y" or Alpha=="Y"):
  a=int(input('enter starting number: '))
  b=int(input('enter ending number: '))
  c=int(input('enter step number: '))
  for i in range(a,b,c):
    print(i)
  else:
    print("Loop ended!!!")
  Alpha=input("You want to continue: ")
else:
  print("Thankyou")
  
#Output:
are you ready in looping y/n :Y
enter starting number: 5
enter ending number: 10
enter step number: 1
5
6
7
8
9
Loop ended!!!
You want to continue: y
enter starting number: 4095
enter ending number: 4120
enter step number: 2
4095
4097
4099
4101
4103
4105
4107
4109
4111
4113
4115
4117
4119
Loop ended!!!
You want to continue: n
Thankyou
