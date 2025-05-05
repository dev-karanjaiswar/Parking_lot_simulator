from func import Parking

def menu(parking_lot):
    print("\n--- Parking System ---")
    print("1. Park your car")
    print("2. Drive out your car")
    print("3. Exit")

    try:
        user_in = int(input("Enter your choice (1/2/3): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return True  # Continue loop

    if user_in == 1:
        parking_lot.parkin()
    elif user_in == 2:
        parking_lot.drive_out()
    elif user_in == 3:
        confo = input("Do you want to exit this system (yes/no): ").strip().lower()
        if confo == "yes":
            print("Exiting the system...")
            return False
        elif confo == "no":
            print("Returning to main menu.")
        else:
            print("Invalid confirmation input.")
    else:
        print("Invalid choice. Please select 1, 2 or 3.")
    
    return True  # Continue loop

if __name__ == "__main__":
    parking_lot = Parking(5)
    running = True
    while running:
        running = menu(parking_lot)
