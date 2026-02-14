a=int(input("Enter the First Number : "))
b=int(input("Enter the Second  Number : "))

print(f"\nAddition : {a+b}")
print(f"Subtraction : {a-b}")
print(f"Multiplication : {a*b}")

if b!=0:
    print(f"Division : {a/b}")
else:
    print("Division by 0 is not possible.")