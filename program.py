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
            print(f"Day {day}: {self.plant1.name} is {height1:.2f} cm and {self.plant2.name} is {height2:.2f} cm")



    def projectTallestDay(self):    #option 3 in menu
        day = 0
        while True:
            day += 1
            height1 = self.plant1.startingHeight + day * self.plant1.growthRate
            height2 = self.plant2.startingHeight + day * self.plant2.growthRate
            if height1 != height2:
                tallest_plant = self.plant1.name if height1 > height2 else self.plant2.name
                print(f"On day {day}, {tallest_plant} becomes taller.")
                break
                

    def run(self):
        self.getPlantInfo()
        while self.running:
            self.displayMenu()
            self.choice = int(input("Enter your choice: "))
        



    print("============ PLANT GROWTH COMPARISON PROGRAM ============")
    print("Welcome! Simulate and compare the growth of two plants.")

    choice = int(input("Enter your choice: "))






