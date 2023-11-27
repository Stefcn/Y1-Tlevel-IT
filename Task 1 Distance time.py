NumberPlate = str(input("What is the NumberPlate?"))
Distance = int(input("What is the Distance?"))
Time = int(input("How long did it take?"))
SpeedLimit = int(input("Enter the speed limit"))

speed = Distance/Time 
 
print ("The Car is travelling", speed, "mph")

if speed > SpeedLimit:
    print(NumberPlate, "is speeding")
elif speed < SpeedLimit:
    print(NumberPlate, "is not speeding")    