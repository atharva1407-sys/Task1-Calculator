print("Welcome to Calculator\n")

print("Select what you want to do Addition , Subtraction , Multiplication & Divison\n")

calculator = input()

match calculator :
    case "Addition":
        print("Enter Numbers you want to Add\n")
        a=int(input("First Number :- "))
        b=int(input("Second Number :- "))
        sum = a + b
        print("Addition of your numbers is :-", sum)

    case "Subtraction":
        print("Enter Numbers you want to Subtract\n")
        a=int(input("First Number :- "))
        b=int(input("Second Number :- "))
        sub = a - b
        print("Addition of your numbers is :-", sub)

    case "Multiplication":
        print("Enter Numbers you want their Product\n")
        a=int(input("First Number :- "))
        b=int(input("Second Number :- "))
        mul = a * b
        print("Addition of your numbers is :-", mul)

    case "Division":
        print("Enter Numbers you want their Division\n")
        a=int(input("First Number :- "))
        b=int(input("Second Number :- "))
        div = a / b
        print("Addition of your numbers is :-", div)

    case _:
        print("Invalid Operator Select between Addition , Subtraction , Multiplication & Divison\n")
