input1 = int(input("Enter the first number : "))
input2 = input("Enter the opration : ")

k = ["/","*","+","-"]

if input2 not in k:
    print("Enter the opration from {/,*,+,-}")
else:
    input3 = int(input("Enter the second number : "))

    if input2 == "+" :
        print("Answer = ",input1+input3)
    
    elif input2 == "-" :
        print("Answer = ",input1-input3)
    
    elif input2 == "*" :
        print("Answer = ",input1*input3)
    
    elif input2 == "/" :
        print("Answer = ",input1/input3)
    