
import csv

class HotelManagementSystem:
    def __init__(self):
        self.bookings = []
        self.rooms_info = {
            "Standard": {"occupancy": 2, "beds": 1, "amenities": ["TV", "Wi-Fi"]},
            "Deluxe": {"occupancy": 4, "beds": 2, "amenities": ["TV", "Wi-Fi", "Mini-bar"]},
            "Suite": {"occupancy": 6, "beds": 3, "amenities": ["TV", "Wi-Fi", "Mini-bar", "Jacuzzi"]}
        }
        self.guest_records = []

    def display_main_menu(self):
        print("Artemis Hotel Management System")
        print("1. Personal Details")
        print("2. Hotel Room Details")
        print("3. Bookings")
        print("4. Billing and Payments")
        print("5. Record Keeping")
        print("6. Exit")

    def get_personal_details(self):
        name = input("Enter your name: ")
        room_type = input("Enter desired room type (Standard/Deluxe/Suite): ")
        return name, room_type

    def display_room_info(self, room_type):
        if room_type in self.rooms_info:
            room_details = self.rooms_info[room_type]
            print("Room Type:", room_type)
            print("Occupancy:", room_details["occupancy"])
            print("Number of Beds:", room_details["beds"])
            print("Amenities:", ', '.join(room_details["amenities"]))
        else:
            print("Room type not found.")

    def make_booking(self, name, room_type):
        check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
        check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
        booking = {"Name": name, "Room Type": room_type, "Check-in Date": check_in_date, "Check-out Date": check_out_date}
        self.bookings.append(booking)
        print("Booking successful.")

    def display_booking_info(self):
        if self.bookings:
            print("Bookings:")
            for idx, booking in enumerate(self.bookings, 1):
                print(f"{idx}. {booking['Name']} - {booking['Room Type']} - {booking['Check-in Date']} to {booking['Check-out Date']}")
        else:
            print("No bookings found.")

    def generate_bill(self, name, room_type):
        
        print("Bill generated for", name)

    def record_guest(self, name, room_type):
        guest_record = {"Name": name, "Room Type": room_type}
        self.guest_records.append(guest_record)
        print("Guest record added.")

    def save_guest_details_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Room Type"])
            writer.writeheader()
            writer.writerows(self.guest_records)
        print("Guest details saved to", filename)

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                name, room_type = self.get_personal_details()
                self.record_guest(name, room_type)
            elif choice == '2':
                room_type = input("Enter room type to display details: ")
                self.display_room_info(room_type)
            elif choice == '3':
                self.display_booking_info()
            elif choice == '4':
                name, room_type = self.get_personal_details()
                self.generate_bill(name, room_type)
            elif choice == '5':
                filename = input("Enter filename to save guest details (e.g., guests.csv): ")
                self.save_guest_details_to_csv(filename)
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    hotel_system = HotelManagementSystem()
    hotel_system.run()