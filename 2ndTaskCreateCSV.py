file = open("CSV writing.csv", "r")

line = file.readline()

Search = input("How do you wish to search for somebody? (name,address,city,phone)")

if Search == ("name") :

    Search = 1

if Search == ("address"):

    Search = 2

if Search == ("city"):

    Search = 3

if Search == ("phone"):

    Search = 4

 

if Search == 1:

    SearchName = input("Please Enter a name:  ")

    found = 0
    
    while(line):

        data = line.split(",")

        if data[0]==SearchName:

            print("Name: ",data[0])

            print("Address: ",data[1])

            print("City: ",data[2])

            print("Phone: ",data[3])

        found = 1

        break

    line=file.readline()

    file.close()

 

if Search == 2:

    SearchName = input("Please Enter a address:  ")

    found = 0

 

    while(line):

        data = line.split(",")

        if data[1]==SearchName:

            print("Name: ",data[0])

            print("Address: ",data[1])

            print("City: ",data[2])

            print("Phone: ",data[3])

        found = 1

        break

    line=file.readline()

    file.close()

 

 

if Search == 3:

    SearchName = input("Please Enter a City:  ")

    found = 0

 

    while(line):

        data = line.split(",")

        if data[2]==SearchName:

            print("Name: ",data[0])

            print("Address: ",data[1])

            print("City: ",data[2])

            print("Phone: ",data[3])

        found = 1

        break

    line=file.readline()

    file.close()

   

if Search == 4:

    SearchName = input("Please Enter a Phonenumber:  ")

    found = 0

 

    while(line):

        data = line.split(",")

        if data[3]==SearchName:

            print("Name: ",data[0])

            print("Address: ",data[1])

            print("City: ",data[2])

            print("Phone: ",data[3])

        found = 1

        break

    line=file.readline()

    file.close()

   

   

 

 

 

 

 

 

 

if found != 1:

    print("not in database")

 

file.close()