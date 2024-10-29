#here will be class with plants information

class PlantInfo:
    name = ""       #what plant name would be
    startingHeight: 0.0     #height with which plant start
    growthRate: 0.0     #how many centimetrs plant grows in 1 day
    numberOfDays: 0  #how many days it'd take to the fastest-growing plant to become bigger than 2nd

    def __init__(self, name="", startingHeight=0.0, growthRate=0.0):
        self.name = name
        self.startingHeight = startingHeight
        self.growthRate = growthRate

