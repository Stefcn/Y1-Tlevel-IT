file = open ("gamerscore.csv","r")
line = file.readline()
SearchName = input("Please enter a name: ")

while(line):
    data =line.split(",")
    if data[0] ==SearchName:
        print( "handle: ",data[0])
        print( "gamerscore: ",data[1])  
    line=file.readline()
if SearchName != data[0]: 
    print("user not found")

file.close()