#Instruction for the file:
#1. Install python 3
#2. Compile and run the file
#3. Follow the prompt
#4. Answer accordingly 

#prompt user if the year is leap or not

try:
    print("Enter the year to determine leap year or not:")
    year = int(input())
    if(year > 0):
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
            print("A leap year!")
        else:
            print("Not a leap year.")
    else:
        raise ValueError
except:
    print("Error, please input the correct value")