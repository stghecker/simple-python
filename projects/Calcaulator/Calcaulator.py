print("==========")
print("Calculator")
print("==========")
print("For Multiplication type 1.")
print("For Addition type 2.")
print("For Division type 3.")
print("For Subtraction type 4.")
OR = int(input("1, 2, 3 OR 4?  :"))

if OR == 1:
    input1 = float(input("First number: ").replace(",", "."))
    input2 = float(input(f"{input1} × ?").replace(",", "."))
    result = input1 * input2
    print("Result:", result)
    print("Reload program to use again")

elif OR == 2:
    input1 = float(input("First number: ").replace(",", "."))
    input2 = float(input(f"{input1} + ?").replace(",", "."))
    result = input1 + input2
    print("Result:", result)
    print("Reload program to use again")

elif OR == 3:
    input1 = float(input("First number: ").replace(",", "."))
    input2 = float(input(f"{input1} + ?").replace(",", "."))
    result = input1 / input2
    print("Result:", result)
    print("Reload program to use again")
    
elif OR == 4:
    input1 = float(input("First number: ").replace(",", "."))
    input2 = float(input(input1 , "- ?").replace(",", "."))
    result = input1 - input2
    print("Result:", result)
    print("Reload program to use again")
    

else:
    print("ERROR")
    
    print("Reload program")

#STGHECKER#
