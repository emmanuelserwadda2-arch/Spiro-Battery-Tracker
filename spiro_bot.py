import datetime
print("====== Spiro Battery Tracker ======")
print("Who are you?")
print("1. Rider")
print("2. Swap Agent")
print("3. Transporter")
print("4. Energy Team")
print("===================================\n")

user_input = input("Enter your role (1-4): ")

if user_input == "1":
    print("Welcome, Rider! Please report your faulty battery.\n")
    rider_name = input("Enter your name: ")
    rider_id = input("Enter your rider ID: ")
    battery_id = input("Enter the battery ID: ")
    number_plate = input("Enter your vehicle number plate: ")
    location = input("Enter your current location: ")
    problem_description = input("Describe the issue: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("faulty_batteries.txt", "a") as file:
        file.write("--- Report ---\n")
        file.write(f"Rider Name: {rider_name}\n")
        file.write(f"Rider ID: {rider_id}\n")
        file.write(f"Battery ID: {battery_id}\n")
        file.write(f"Number Plate: {number_plate}\n")
        file.write(f"Location: {location}\n")
        file.write(f"Problem Description: {problem_description}\n")
        file.write(f"Timestamp: {timestamp}\n\n")
    print("Report submitted successfully!")
    print(f"Battery {battery_id} has been logged.")
    print("Please drop the battery at the nearest swap station.")

elif user_input == "2":
    print("Welcome, Swap Agent! You can log a battery drop off.")
    agent_name = input("Enter your name: ")
    station_id = input("Enter the swap station ID: ")
    battery_id = input("Enter the battery ID being dropped off: ")
    rider_name = input("Enter the rider's name who dropped the battery: ")
    problem_description = input("Describe the issue with the battery (if any): ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("battery_drops.txt", "a") as file:
        file.write("--- Drop Off Report ---\n")
        file.write(f"Agent Name: {agent_name}\n")
        file.write(f"Station ID: {station_id}\n")
        file.write(f"Battery ID: {battery_id}\n")
        file.write(f"Rider Name: {rider_name}\n")
        file.write(f"Problem Description: {problem_description}\n")
        file.write(f"Timestamp: {timestamp}\n\n")
    print("Drop off report submitted successfully!")
    print(f"Battery {battery_id} has been logged.")
    print("Please ensure the battery is properly stored and labelled at the swap station.")

elif user_input == "3":
    print("Welcome, Transporter! You can log batteries being collected.")
    transporter_name = input("Enter your name: ")
    vehicle_id = input("Enter your vehicle ID: ")
    battery_ids = input("Enter the battery IDs being collected (comma separated): ")
    battery_id_list = [bid.strip() for bid in battery_ids.split(",")]
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("battery_collections.txt", "a") as file:
        file.write("--- Collection Report ---\n")
        file.write(f"Transporter Name: {transporter_name}\n")
        file.write(f"Vehicle ID: {vehicle_id}\n")
        file.write(f"Battery IDs: {', '.join(battery_id_list)}\n")
        file.write(f"Timestamp: {timestamp}\n\n")
    print("Collection report submitted successfully!")
    print(f"{len(battery_id_list)} battery/batteries logged for collection.")

elif user_input == "4":
    print("Welcome, Energy Team! You can confirm warehouse receipt.\n")
    team_member_name = input("Enter your name: ")
    warehouse_id = input("Enter the warehouse ID: ")
    battery_ids = input("Enter the battery IDs received (comma separated): ")
    battery_id_list = [bid.strip() for bid in battery_ids.split(",")]
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("warehouse_receipts.txt", "a") as file:
        file.write("--- Warehouse Receipt Report ---\n")
        file.write(f"Team Member Name: {team_member_name}\n")
        file.write(f"Warehouse ID: {warehouse_id}\n")
        file.write(f"Battery IDs: {', '.join(battery_id_list)}\n")
        file.write(f"Timestamp: {timestamp}\n\n")
    print("Warehouse receipt submitted successfully!")
    print(f"{len(battery_id_list)} battery/batteries logged as received.")
else:
    print("Invalid input. Please enter a number between 1 and 4.")