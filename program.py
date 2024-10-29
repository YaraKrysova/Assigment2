from plantInformation import PlantInfo

class Program:
    def __init__(self):
        self.plant1 = PlantInfo()
        self.plant2 = PlantInfo()
        self.running = True
    
    def getPlantInfo(self):
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

    def projectGrowth(self, days):  #option 2 in menu
        print("Projected growth over time:")
        for day in range(1, days + 1):
            height1 = self.plant1.startingHeight + day * self.plant1.growthRate
            height2 = self.plant2.startingHeight + day * self.plant2.growthRate
            print(f"Day {day}: {self.plant1.name} is {height1:.1f} cm and {self.plant2.name} is {height2:.1f} cm")



    def projectTallestDay(self):    #option 3 in menu
        day = 0
        while True:
            # Calculate the height for each plant on the current day
            height1 = self.plant1.startingHeight + day * self.plant1.growthRate
            height2 = self.plant2.startingHeight + day * self.plant2.growthRate
            
            # Display the heights for the current day
            print(f"{day}: {self.plant1.name} is {height1:.1f} cm and {self.plant2.name} is {height2:.1f} cm tall.")
            
            if height1 != height2:
                fastestGrowingPlant1 = self.plant1.growthRate > self.plant2.growthRate #this way we will indicate which plant grows faster
                tallerPlant = self.plant1.name if (height1 > height2) and fastestGrowingPlant1 else self.plant2.name
                day += 1
                print(f"After {day} day(s), {tallerPlant} will be taller than the other.")
                break
            
                

    def run(self):
        print("============ PLANT GROWTH COMPARISON PROGRAM ============")
        print("Welcome! Simulate and compare the growth of two plants.")
        self.getPlantInfo()
        while self.running:
            self.displayMenu()
            self.choice = int(input("Enter your choice: "))
        

            if self.choice == 1:
                print("Plant Information:")
                print(f"{self.plant1.name} is {self.plant1.startingHeight} cm tall and has a daily growth rate of {self.plant1.growthRate} cm per day")
                print(f"{self.plant2.name} is {self.plant2.startingHeight} cm tall and has a daily growth rate of {self.plant2.growthRate} cm per day")
            
            elif self.choice == 2:
                days = int(input("Enter the number of days for growth projection: "))
                self.projectGrowth(days)
            
            elif self.choice == 3:
                self.projectTallestDay()
            
            elif self.choice == 4:
                self.getPlantInfo()
            
            elif self.choice == 5:
                print("Have a great day!")
                self.running = False
            
            else:
                print("Invalid choice. Please select a valid option.")


program = Program()
program.run()






