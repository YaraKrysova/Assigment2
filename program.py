from plantInformation import PlantInfo

class Program:
    def __init__(self):
        self.plant1 = PlantInfo()
        self.plant2 = PlantInfo()
        self.running = True
    
    def get_plant_info(self):
        print("First plant...")
        self.plant1.name = input("Name: ")
        self.plant1.startingHeight = float(input("Starting height (cm): "))
        self.plant1.growthRate = float(input("Daily growth rate (cm): "))

        print("Second plant...")
        self.plant2.name = input("Name: ")
        self.plant2.startingHeight = float(input("Starting height (cm): "))
        self.plant2.growthRate = float(input("Daily growth rate (cm): "))


    def displayMenu(self):
        print("**Menu**")
        print("1) Display plant information")
        print("2) Projected growth over time")
        print("3) Project day when plant with fastest growth rate is tallest")
        print("4) Change plant information")
        print("5) Quit program")

    def projectGrowth(self, days):
        print("Projected growth over time:")
        for day in range(1, days + 1):
            height1 = self.plant1.startingHeight + day * self.plant1.growthRate
            height2 = self.plant2.startingHeight + day * self.plant2.growthRate
            print(f"Day {day}: {self.plant1.name} is {height1:.2f} cm and {self.plant2.name} is {height2:.2f} cm")



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
        
        elif choice == 4:
            print("First plant...")
            plant1.name = input("Name: ")
            plant1.startingHeight = int(input("Starting height (cm): "))
            plant1.growthRate = int(input("Daily growth rate: "))

            print("Second plant...")
            plant2.name = input("Name: ")
            plant2.startingHeight = int(input("Starting height (cm): "))
            plant2.growthRate = int(input("Daily growth rate: "))

        elif choice == 5:
            break


    print("============ PLANT GROWTH COMPARISON PROGRAM ============")
    print("Welcome! Simulate and compare the growth of two plants.")

    choice = int(input("Enter your choice: "))






