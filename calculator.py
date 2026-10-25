print("---Simple Calculator(type 'q' to quit)---")


while True:
    num1_input=input("\nEnter first number (or 'q' to quit):")
    if num1_input.lower()=='q':
        print("Bye! Calculator closed.")
        break

    try:
        num1=float(num1_input)
        op=input("Enter operation(+,-,*,/):")
        num2=float(input("Enter the second number:"))


        if op=='+':
            result=num1+num2
            print(f"\nResult:{num1} + {num2} = {result}")

        elif op=='-':
            result=num1-num2
            print(f"\nResult:{num1} - {num2} = {result}")

        elif op=='*':
            result=num1*num2
            print(f"\nResult:{num1} * {num2} = {result}")

        elif op=='/':
            if num2==0:
                print("Cannot divide by zero!")
            else:
                result=num1/num2
                print(f"\nResult:{num1} / {num2} = {result}")
        else:
            print("Invalid operation!")
    except ValueError:
        print("Please enter valid numbers!")