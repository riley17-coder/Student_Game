

def surfing(points, weather_today):

    """
    performs surfing, mass, ice cream
    input: user preference
    output: points earned
    
    """
    import time
    import random
    surfing = input("Would you like to surf the morning tides on Newport Beach before your first class?(yes/no): ").lower()
    if surfing == "yes" and weather_today in ["sunny", "windy", "rainy"]:
        #proceed to running the surfing block
        print("Good choice! Let's go to Newport Beach with a 10-minute helicopter ride")
        print("...")
        #pause for 2 seconds to increase sense of reality
        time.sleep(2)
        print("Now we are at Newport Beach. Enjoy the chilly water!")
        points += 15
        wave_catches = int(input("How many waves do you plan to catch this morning?:"))
        actual_wave_catches = random.randint(5,20)
        if wave_catches == actual_wave_catches:
            print(f"Good guess! You were able to catch exactly {wave_catches} waves!")
            points += 10
        else:
            print(f"Not exactly what we have planned, but nice try! You were able to catch {actual_wave_catches}waves!")
        time.sleep(3)

        #proceed to daily mass block
        mass = input("It is now 7AM. Would you join the monks at the Abbey nearby for morning mass? (yes/no):").lower()
        if mass == "yes":
            points += 10
            print("Good kid! You attended mass and earned a pat on the shoulder from the Abbot, saying: “You have been a faithful servant today!”")
        else:
            print("That's okay. You can still attend daily night mass back in St.Joseph's chapel at holy cross!")

        #proceed to the ice cream shop block
        icecream = input("Now you may stop by Clemie's Ice Cream before taking the helicopter back. Would you like that? (yes/no):").lower()
        if icecream == "yes":
            flavor = input("Please order a flavor from black raspberry, coffee, maple walnut, vegan vanilla")
            print(f"Good choice of fats. Your {flavor} order will be served soon. 600 calories intake and morning insulin spike is acheived!")
            points -= 5
        else:
            print("You resisted temptation and made the healthy chioce!")
            points += 5
   
    
    elif surfing == "yes" and weather_today not in ["sunny", "windy", "rainy"]:
            #surfing is not validated so user will be prompted to study python instead
            print(f"The weather is {weather_today}, so surfing is not safe.")
            print(" You may go to study for python instead!")
    else:
        #user does not wish to surf, so they will study python
        print("You decided not to surf.")
        print(" You may go to study for python instead!")
        points += 10

    return points