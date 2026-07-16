print()
print("=========== CALCULATOR PROJECT ===========\n")

while True:
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modular\n6.Exit(Type Q)\n")
    num = input("Enter Your Choice : ")
    if num.lower() == 'q':
        print("Thamks for Using My Calsi")
        break
    else:
        print() 
        a,b = input("Enter Two Numbers : ").split()
        a ,b = int(a),int(b)
        if num ==  "1":
            print("Sum = ",a+b)
        elif num == "2":
            print("difference = ",a-b)
        elif num == "3":
            print("mul =",a*b)
        elif num == "4":
            print("div = ",a/b)
        elif num == "5":
            print('mod = ',a%b)
        else:
            print("Invalid Input")