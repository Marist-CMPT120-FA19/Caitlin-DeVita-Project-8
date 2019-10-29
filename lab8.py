#Caitlin De Vita
#caitlin.devita1@marist.edu
#This program prints the number of cooling degree days and heating degree days.
#If the average temperature for a day is below 60,  then the number of degrees below 60 is added to the heating degree days.
#If the temperature is above 80, the amount over 80 is added to the cooling degree days. 


def main():
        temp = input("Enter the average tempurature per day separated by commas: ")
        temp = temp.split(",")
        coolDays = 0
        heatDays = 0

        for x in temp:
            if float(x) > 80 or float(x) < 60:
                if int(x) > 80:
                    coolDays += float(x) - 80
                else:
                    heatDays += 60 - float(x)

        print("There are", coolDays, "cooling degrees days and there are", heatDays, "heating degrees days.")
        
main()
