import math
exam1 = float(input("enter your marks in subject1"))
exam2 = float(input("enter your marks in subject2"))
sport1 = float(input("enter your marks in sports activity"))
activity1 = float(input("enter your marks in activity1"))
activity2 = float(input("enter your marks in activity2"))
exam = (exam1+exam2)*50/100
sports = (sport1*(30/100))
activity = ((activity1+activity2)*20/100)
total = exam+sports+activity
print("Your Result is" ,total)
