while True:
    username = str(input("username"))
    password = str(input("password"))

    if username == "Admin"and password == "Password":
        print ("login successful")
        break
    else: print ("wrong password or username")

