from plantInformation import PlantInfo

class Program:
    plant1 = PlantInfo()

    plant2 = PlantInfo()
    
    print("============ PLANT GROWTH COMPARISON PROGRAM ============")
    print("Welcome! Simulate and compare the growth of two plants.")
    print("First plant...")
    plant1.name = input("Name: ")
    plant1.startingHeight = int(input("Starting height (cm): "))
    plant1.growthRate = int(input("Daily growth rate: "))

    plant2.name = input("Name: ")
    plant2.startingHeight = int(input("Starting height (cm): "))
    plant2.growthRate = int(input("Daily growth rate: "))

