class Parking:
    def __init__(self, available_spots):
        self.available_spots = available_spots
        self.total_spots = available_spots

    def parkin(self):
        if self.available_spots > 0:
            print(f"Parking... Spots before: {self.available_spots}")
            self.available_spots -= 1
            print(f"Spots left: {self.available_spots}")
        else:
            print("Sorry, no spots available!")

    def drive_out(self):
        if self.available_spots < self.total_spots:
            print(f"Driving out... Spots before: {self.available_spots}")
            self.available_spots += 1
            print(f"Spots now: {self.available_spots}")
        else:
            print("All spots are already free.")
