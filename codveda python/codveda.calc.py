print("Addition")
print("Subtraction")
print("Division")
print("Multiplication")

#list of operations

operations=["addition", "subtraction","division", "multiplication"]

#ask user for choice of operation
user_choice=str(input("enter arithimetic operation: ").lower().strip())
#define our functions for respective operations

#addition function
def add():
    if user_choice in operations and user_choice =="addition":
        #create a variable to store user input
        first_num=float(input("enter first number: "))
        second_num=float(input("enter second number: "))
        result=first_num + second_num
        print(f"Result is  {result}")

        
#subtraction function
def subtract():
    if user_choice in operations and user_choice =="subtraction":
        #create a variable to store user input
        first_num=float(input("enter first number: "))
        second_num=float(input("enter second number: "))
        result=first_num - second_num
        print(f"Result is  {result}")

        
#division function
def division():
        #create a variable to store user input
        first_num=float(input("enter first number: "))
        second_num=float(input("enter second number: "))
        if user_choice in operations and user_choice =="division":
             #include my invalid condition 
            if second_num==0:
                print("sadly, that is an error")
            
            else:
            
                result=first_num / second_num
                print(f"Result is  {result}")
      


#multiplication function
def multiply():
    if user_choice in operations and user_choice =="multiplication":
        #create a variable to store user input
        first_num=float(input("enter first number: "))
        second_num=float(input("enter second number: "))
        result=first_num * second_num
        print(f"Result is  {result}")

#we call all the functions


if user_choice=="addition":
    add()
elif user_choice == "subtraction":
    subtract()
    
elif user_choice=="division":
    division()
elif user_choice == "multiplication" :
    multiply()
else:
    print("Invalid Input")

print("Thanks for using my calculator")