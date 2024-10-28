from plantInformation import PlantInfo

class Program:
    plant1 = PlantInfo()

    plant2 = PlantInfo()
    
    print("============ PLANT GROWTH COMPARISON PROGRAM ============")
    print("Welcome! Simulate and compare the growth of two plants.")
    print("First plant...")
    plant1.name = input("Name: ")
    plant1.startingHeight = input("Starting height (cm): ")
    plant1.growthRate = input("Daily growth rate: ")



