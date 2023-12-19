import datetime
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Task_4a.csv')


def mainmenu():
  print("\t\t****Welcome to the Dashboard****")
  print('1) Return all current data')
  print('2) Return data for a specific region')
  print('3) Select property type') 
  return int(input(""))


def alldata():
  print(df)



def select_property_type(property_type):
    specific_property = df[df['Property Type'] == property_type]
    print (specific_property)
    return specific_property



def region_check(region, startdate, enddate):  # region, startdate, enddate

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    plt.show()
    return result


x = mainmenu()
while x == 1 or x == 2 or x == 3:
    if x == 1:
        alldata()

    elif x == 2:
        while True:
            print()
    elif x == 3:
      property_type = input("select a property type")
      select_property_type(property_type)

    region = input("Please enter the name of the region you would like to check:")
    region = region.capitalize()
    if region in df.Region.values:
        while True:
            startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20")
            startdate = startdate.capitalize()
            if startdate not in df.columns:
                print("Error start date not found")
            else:
                while True:
                    enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20")
                    enddate = enddate.capitalize()
                    if enddate not in df.columns:
                        print("Error end date not found")
                    else:
                        region_check(region, startdate, enddate)
                        break
                break
        else:
            print("Region not found")
    x = mainmenu()

