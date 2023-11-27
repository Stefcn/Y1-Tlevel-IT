Competitions = 0
while Competitions !=1: 
    CompetiotionType = input(str("what competition would you like to compete in Chess, Billards, Darts"))
    if CompetiotionType == "Chess":
        Comepteitions = 1
    elif CompetiotionType == "Billards":
        Competitions = 1
    elif CompetiotionType == "Darts":
        Competitions = 1
    else:
        print ("Incorrect value")    

