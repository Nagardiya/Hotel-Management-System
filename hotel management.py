                                                                                                               # ---------- Menu dictionary ----------
menu = {
    "A": "Show Room (with Rent)",
    "B": "Customer Ability (Check Affordable Rooms)",
    "C": "Add Room No",
    "D": "Detail Of Room No",
    "E": "Exit"
}
print(menu)


# ---------- Function to Create Rooms ----------
def init_rooms():
    rooms = {}
    for i in range(1, 11):
        rent = 300 if i <= 3 else 650 if i <= 6 else 900
        rooms[i] = {"Status": "Not Occupied", "Name": "", "Mobile": "", "City": "", "Rent": rent}
    return rooms


# ---------- Other Functions ----------
def show_menu():
    print("\nHotel Management Menu:")
    for key, value in menu.items():
        print(f"{key} = {value}")


def show_rooms(rooms):
    print("\nRoom Status with Rent:")
    for room_no, detail in rooms.items():
        print(f"Room {room_no}: {detail['Status']} | Rent: Rs.{detail['Rent']}")


def customer_ability(rooms):
    while True:
        try:
            room_no = int(input("\nEnter Room Number (1-10): "))
            if room_no not in rooms:
                print("Invalid Room Number!")
                continue

            budget = int(input("Enter your available amount (in Rs): "))
        except ValueError:
            print("Please enter valid numeric values!")
            continue

        if rooms[room_no]["Status"] == "Occupied":
            print(f"Room {room_no} is already occupied.")
        else:
            rent = rooms[room_no]["Rent"]
            if budget >= rent:
                days = budget // rent
                remaining = budget % rent
                print(f"\nRoom {room_no} is available for {days} day(s).")
                print(f"Remaining balance: Rs.{remaining}")
            else:
                print(f"\nYou don't have enough money for Room {room_no}.")
                print(f"Room rent is Rs.{rent}, but you only have Rs.{budget}.")

        again = input("\nDo you want to check another room? (Yes/No): ").strip().lower()
        if again != "yes":
            break


def add_room(rooms):
    room_no = int(input("Enter Room Number (1-10): "))
    if room_no not in rooms:
        print("Invalid Room Number!")
        return
    if rooms[room_no]["Status"] == "Not Occupied":
        name = input("Enter Customer Name: ")
        mobile = input("Enter Mobile No: ")
        city = input("Enter City: ")
        rooms[room_no].update({"Status": "Occupied", "Name": name, "Mobile": mobile, "City": city})
        print(f"Room {room_no} occupied!")
    else:
        print("It is already Occupied.")


def room_detail(rooms):
    room_no = int(input("Enter Room Number (1-10) to Check Detail: "))
    if room_no in rooms:
        detail = rooms[room_no]
        print(f"\nRoom {room_no} Details:")
        print(f"Status: {detail['Status']}")
        print(f"Rent: Rs.{detail['Rent']}")
        if detail['Status'] == "Occupied":
            print(f"Name: {detail['Name']}")
            print(f"Mobile: {detail['Mobile']}")
            print(f"City: {detail['City']}")
    else:
        print("Invalid Room Number!")


# ---------- Main Program ----------
def main():
    rooms = init_rooms()
    while True:
        show_menu()
        choice = input("\nEnter your choice: ").upper()

        if choice == "A":
            show_rooms(rooms)
        elif choice == "B":
            customer_ability(rooms)
        elif choice == "C":
            add_room(rooms)
        elif choice == "D":
            room_detail(rooms)
        elif choice == "E":
            print("Exiting the program.")
            break
        else:
            print("This option not active yet.")


# ---------- Run ----------
if __name__ == "__main__":
    main()