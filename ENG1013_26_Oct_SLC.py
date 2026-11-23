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
            function returns a dictionary with values overSpeed and penalties:
                overSpeed: difference between speed of vehicle and speed limit of road 
                penalties: is a list containing the demerit, suspension and fine values
    """

    result = {
        "overSpeed": roadSpeed - speedLimit,
        "penalties": [0, 0, 0.00],  # [demerit, suspension, fine]
    }
    
    result["overSpeed"] = round(roadSpeed - speedLimit, 2)
    roundedOverSpeed = int(result["overSpeed"])

    if vehType:
        if 0 < roundedOverSpeed < 10:
            result["penalties"] = [1, 0, 324.00]
        elif 10 <= roundedOverSpeed < 15:
            result["penalties"] = [3, 0, 509.00]
        elif 15 <= roundedOverSpeed < 25:
            result["penalties"] = [3, 0, 740.00]
        elif 25 <= roundedOverSpeed < 30:
            result["penalties"] = [0, 3, 1017.00]
        elif 30 <= roundedOverSpeed < 35:
            result["penalties"] = [0, 3, 1294.00]
        elif 35 <= roundedOverSpeed < 40:
            result["penalties"] = [0, 6, 1572.00]
        elif 40 <= roundedOverSpeed < 45:
            result["penalties"] = [0, 6, 1849.00]
        elif 45 <= roundedOverSpeed:
            result["penalties"] = [0, 12, 2127.00]
        if 10 <= roundedOverSpeed < 25 and speedLimit > 100:
            result["penalties"] = [0, 3, 740.00]

    else:
        if 0 < roundedOverSpeed < 10:
            result["penalties"] = [1, 0, 247.00]
        elif 10 <= roundedOverSpeed < 25:
            result["penalties"] = [3, 0, 395.00]
        elif 25 <= roundedOverSpeed < 30:
            result["penalties"] = [0, 3, 543.00]
        elif 30 <= roundedOverSpeed < 35:
            result["penalties"] = [0, 3, 642.00]
        elif 35 <= roundedOverSpeed < 40:
            result["penalties"] = [0, 6, 741.00]
        elif 40 <= roundedOverSpeed < 45:
            result["penalties"] = [0, 6, 840.00]
        elif 45 <= roundedOverSpeed:
            result["penalties"] = [0, 12, 988.00]
        if 10 <= roundedOverSpeed < 25 and speedLimit > 100:
            result["penalties"] = [0, 3, 395.00]

    return result


#Ensures input is correct and calls calc_penalty
def main():
    """
    Ensures input is correct before calling calc_penalty
            Parameters:
                Has no parameters
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
            overSpeed = result["overSpeed"]
            demerit = result["penalties"][0]
            suspension = result["penalties"][1]
            fine = result["penalties"][2]

            if demerit == 0:
                demerit = "None"
            if suspension == 0:
                suspension = "None"
            if fine == 0:
                fine = "None"
            
            print(f"overSpeed: {overSpeed:.2f}\nDemerit: {demerit}\nSuspension: {suspension}\nFine: {fine}")

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