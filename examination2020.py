f = open("C:\\Users\\Malinga\\Desktop\\python\\data.txt", 'r')

found = False
highRisk = False
countNumberRiskCountries = 0

countries = ["China", "South", "Korea", "Italy", "Iran"]
passportNumber = input("Enter Passport Number Here: ")

for line in f:
    data = []
    data = line.strip().split(',')
    
    if passportNumber in data:
        found = True
        
        
        for c in countries:
            
            if c in data:
                highRisk = True
                countNumberRiskCountries += 1
                print("High Risk Traveler")
                break

        if highRisk:
            print("He/She has visited about "+ str(countNumberRiskCountries)+ " Countries")    
        else:
          print("Low Risk Traveler")
        break         

if not found:
    print("Invalid Passport number")
f.close()    