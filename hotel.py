# Hotel Management System in Python (Text-Based, Menu-Driven)
import os
import time

rooms = {}

# Pre-fill rooms with empty status
for i in range(101, 111):
    rooms[i] = {'name': None, 'days': 0, 'amount': 0, 'status': 'Available'}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_rooms():
    print("\nRoom Status:")
    for num, info in rooms.items():
        print(f"Room {num} - {info['status']}")

def check_in():
    try:
        room_no = int(input("Enter room number to check-in (101-110): "))
        if room_no not in rooms:
            print("Invalid room number!")
            return
        if rooms[room_no]['status'] == 'Occupied':
            print("Room is already occupied!")
            return

        name = input("Enter guest name: ")
        days = int(input("Number of days to stay: "))
        amount = days * 1000  # Example rate

        rooms[room_no] = {
            'name': name,
            'days': days,
            'amount': amount,
            'status': 'Occupied'
        }
        print(f"Check-in successful! Total bill: Rs. {amount}")
    except ValueError:
        print("Invalid input. Try again.")

def check_out():
    try:
        room_no = int(input("Enter room number to check-out: "))
        if room_no not in rooms or rooms[room_no]['status'] == 'Available':
            print("Room is not occupied.")
            return

        print(f"Guest: {rooms[room_no]['name']}")
        print(f"Days stayed: {rooms[room_no]['days']}")
        print(f"Total Bill: Rs. {rooms[room_no]['amount']}")
        confirm = input("Confirm checkout? (y/n): ")
        if confirm.lower() == 'y':
            rooms[room_no] = {'name': None, 'days': 0, 'amount': 0, 'status': 'Available'}
            print("Checked out successfully.")
        else:
            print("Checkout cancelled.")
    except ValueError:
        print("Invalid input. Try again.")

def room_details():
    try:
        room_no = int(input("Enter room number to view details: "))
        if room_no not in rooms:
            print("Invalid room number.")
            return

        info = rooms[room_no]
        print("\n--- Room Info ---")
        print(f"Room Number: {room_no}")
        print(f"Status: {info['status']}")
        if info['status'] == 'Occupied':
            print(f"Guest Name: {info['name']}")
            print(f"Days Staying: {info['days']}")
            print(f"Bill Amount: Rs. {info['amount']}")
    except ValueError:
        print("Invalid input. Try again.")

def main():
    while True:
        print("""
========= Hotel Management =========
1. View Room Status
2. Check-in
3. Check-out
4. View Room Details
5. Exit
        """)
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_rooms()
        elif choice == '2':
            check_in()
        elif choice == '3':
            check_out()
        elif choice == '4':
            room_details()
        elif choice == '5':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

        input("\nPress Enter to continue...")
        clear()

if __name__ == '__main__':
    main()
