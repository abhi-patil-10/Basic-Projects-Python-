try:
    while(True) :
        
        a = int(input("Enter the first number :"))
        b = int(input("Enter the second number :"))
        
      

        print("Enter the operation Do you want to perform \n Press + for addition \n Press - for Subtraction \n Press * Multiplication \n Press / for Division  \n Press x for Exit ")

        o = input("Enter the operation :")
        match o:
            case "+":
                print(f"The result is {a+b}")
            case "-":
                print(f"The result is {a-b}")
            case "*":
                print(f"The result is {a*b}")
            case "/":
                print(f"The result is {a/b}")
            case "x":
                break
            case default:
                print("Invalid Operation ")
except Exception as e :
    print("Error : ",e)