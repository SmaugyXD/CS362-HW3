#Instruction for the file:
#1. Install python 3
#2. Compile and run the file
#3. Follow the prompt
#4. Answer accordingly 

#prompt user if the year is leap or not
print("Enter the year to determine leap year or not:")
year = int(input())
noLeap = "Not a leap year."
Leap = "A leap year!"


if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(Leap)
else:
    print(noLeap)