
print("**Menu**")

print("1) Display plant information")
print("2) Projected growth over time")
print("3) Project day when plant with fastest growth rate is tallest")
print("4) Change plant information")
print("5) Quit program")

choice = int(input("Enter your choice: "))

if choice == 1:
    print(f"{plant1.name} is {plant1.startingHeight} cm tall and has a daily growth rate of {plant1.growthRate} cm per day")
    print(f"{plant2.name} is {plant2.startingHeight} cm tall and has a daily growth rate of {plant2.growthRate} cm per day")

        
elif choice == 2:
    days = int(input("How many days of growth? "))
    x = 1
        while x < days:
            heightOnXDay1 = plant1.startingHeight + plant1.growthRate
            heightOnXDay2 = plant2.startingHeight + plant2.growthRate
            print(f"{x}: {plant1.name} is {heightOnXDay1} and {plant2.name} is {heightOnXDay2}")
            x = x + 1
