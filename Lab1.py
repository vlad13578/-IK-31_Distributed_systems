import datetime

def Factorial(n):
    ft=1;
    for i in range(1,n+1,1):
        ft = ft * i
    return ft

print("HELLo World!")
Name = input("Please, enter your name: ")
print("Hello, " + Name + "!")
Lenght = len(Name)
print("Your name has " + str(Lenght) + " letters.")
print(str(Lenght) + "! = " + str(Factorial(Lenght)))

Day, Month, Year = input("Please, enter your birth date in format (DD.MM.YYYY): ").split('.')
Real_Data = datetime.datetime.now()
Birth_Data = datetime.datetime(year=int(Year), month=int(Month), day=int(Day))
Age_Time = Real_Data - Birth_Data
Age_Year = int(Age_Time.days/365)
print("Today is " + Real_Data.strftime("%d.%m.%Y"))
print("You are " + str(Age_Year) + " year (" + str(Age_Time.days) + " days) old.")

