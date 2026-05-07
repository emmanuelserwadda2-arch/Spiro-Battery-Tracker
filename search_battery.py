search_id = input("Enter the battery ID to search for: ")
found = False

files = [
    ("faulty_batteries.txt", "Faulty Batteries"),
    ("battery_drops.txt", "Battery Drops"),
    ("battery_collections.txt", "Battery Collections"),
    ("warehouse_receipts.txt", "Warehouse Receipts"),
]

for filename, label in files:
    try:
        with open(filename, "r") as file:
            content = file.read()
        for report in content.strip().split("\n\n"):
            if search_id in report:
                print(f"\n[{label}]")
                print(report)
                found = True
    except FileNotFoundError:
        pass

if not found:
    print(f"No records found for battery ID: {search_id}")
