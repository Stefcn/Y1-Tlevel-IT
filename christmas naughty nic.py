name = input("Enter Name: ")
address = input("Enter address")
postcode = input("Enter Postcode")
total =int(input("Enter total score"))

filename = "Naughty.txt" if total < 0 else "Nice.txt"
with open(filename,"a") as file:
    file.write(f"Name: {name}, Address: {address}, Postcode {postcode}, Score {total}\n")