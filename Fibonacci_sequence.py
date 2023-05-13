length=int(input("Enter Fibonacci: "))
num1, num2 = 0, 1
print("Fibonacci sequence:")
for i in range(length):
    print(num1, end="  ")
    res = num1 + num2
    num1 = num2
    num2 = res

#Output:
Enter Fibonacci: 15
Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34  55  89  144  233  377  
