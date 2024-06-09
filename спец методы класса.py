class House():
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

brik = House()

brik.setNewNumberOfFloors(9)

print(brik.numberOfFloors)

