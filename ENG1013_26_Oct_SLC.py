# Author name: Mayan Manohar
# Last modified date: 18/11/2026
# File version number = 3.0

#calculates the penalty and returns dict in [demerit, suspension, fine] format
def calc_penalty(vehType, roadSpeed, speedLimit):
    """
    Used to calculate the penalties the person faces depending on their speeding value
        Parameters:
            vehType (bool): Is vehicle heavy? True if yes, False if no
            roadSpeed (float): Speed of vehicle
            speedLimit (integer): Speed limit of the road
        Returns:
            function returns a dictionary with values overspeed and penalty:
                overspeed: difference between speed of vehicle and speed limit of road 
                penalty: is a list containing the demerit, suspension and fine values
    """

    result = {
        "overspeed": roadSpeed - speedLimit,
        "penalties": [0, 0, 0.00],  # [demerit, suspension, fine]
    }

    overSpeed = int(roadSpeed - speedLimit)
    
    if overSpeed <= 0:
        return result

    #(minimum overspeed, fine, demerit points, suspension).
    penalties1 = [
        (0, 0.00, 0, 0),
        (10, 247.00, 1, 0),
        (25, 395.00, 3, 0),
        (30, 543.00, 0, 3),
        (35, 642.00, 0, 3),
        (40, 741.00, 0, 6),
        (45, 840.00, 0, 6)
    ]

    penalties2 = [
        (0, 0.00, 0, 0),
        (10, 324.00, 1, 0),
        (15, 509.00, 1, 0),
        (25, 740.00, 3, 0),
        (30, 1017.00, 0, 3),
        (35, 1294.00, 0, 3),
        (40, 1572.00, 0, 6),
        (45, 1849.00, 0, 6)
    ]

    if vehType:
        for i in range(6):
            if penalties2[i][0] <= overSpeed < penalties2[i+1][0]:
                result["penalties"] = [ [penalties2[i+1][1]], [penalties2[i+1][2]], [penalties2[i+1][3]] ]
            if speedLimit > 100 and 10 <= overSpeed < 25:
                result["penalties"] = [0, 3, 395.00]
            if overSpeed > 45:
                result["penalties"] = [0, 12, 988.00]
    else:
        for i in range(6):
            if penalties1[i][0] <= overSpeed < penalties1[i+1][0]:
                result["penalties"] = [ [penalties1[i+1][1]], [penalties1[i+1][2]], [penalties1[i+1][3]] ]
            if speedLimit > 100 and 10 <= overSpeed < 25:
                result["penalties"] = [0, 3, 740.00]
            if overSpeed > 45:
                result["penalties"] = [0, 12, 2127.00]

    return result

#Ensures input is correct and calls calc_penalty
def main():
    """
    Ensures input is correct before calling calc_penalty
            Parameters:
                None
            Returns:
                returns nothing
    """
    noInterrupt = True
    boolHeavy = -1
    speedLimit = -1
    roadSpeed = -1
    try: 
        while noInterrupt:
            #Find if vehicle is heavy 
            while True:
                boolHeavy = str(input("Are you driving a heavy vehicle[Y/N]: ")).strip().upper()
                if boolHeavy != "Y" and boolHeavy != "N":
                    print("404: Enter an appropriate value")
                else:
                    if boolHeavy == "Y":
                        boolHeavy = True
                    else:
                        boolHeavy = False
                    break

            #Find speed limit
            while True:
                try:
                    speedLimit = int(input("What is the road speed limit: "))
                    if speedLimit > 0:
                        break
                except ValueError:
                        print("404: enter an appropriate value")

            #Find speed of vehicle
            while True:
                try:
                    roadSpeed = float(input("What is the speed of your vehicle: "))
                    if roadSpeed > 0:
                        break
                except ValueError:
                    print("404: enter an appropriate value")

            #call calc_penalty and print result
            result = calc_penalty(boolHeavy, roadSpeed, speedLimit)

            while True:
                try:
                    choice = str(input("Would you like to check for another vehicle [Y/N]: "))
                    if choice == "N":
                        noInterrupt = False
                        break
                    elif choice == "Y":
                        break
                except ValueError:
                    print("404: enter an appropriate value")
                
    except KeyboardInterrupt:
        print("\nUser Keyboard Interrupt - Exiting")

if __name__ == "__main__":
    main()