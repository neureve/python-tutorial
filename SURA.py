a = float(input("Enter a number; "))
op = input("Enter operator; ")
b = float(input("enter number; "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
        if b != 0:
             print (a / b)
        else:
             print("syntax error")
else:
     print("invalid operator")
