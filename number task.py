file = open("gamerscore.csv", "r")
line = file.readline()

 

while(line):
    data =line.split(",")
    if int(data[1]) <= 6000:
        print("Handle: ",data[0])
    line=file.readline()

 

file.close()