num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
print(f"{num1}x{num2}={num1*num2}")
if(num1*num2)>0:
    print("The result is positive.")
elif num1 * num2 < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")