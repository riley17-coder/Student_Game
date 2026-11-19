import random
import time
from surf_module import surfing
print("Welcome to a day in the life of a holycross student")
points = 0
print("You start everyday with 0 points")
print("Good morning! It is 3 a.m. Your alarm is ringing...")

get_up_choice = input("Do you wish to get up? (yes/no): ").lower()
get_up = get_up_choice


def wake_up_early(points):
    """
    Run the part of code that happens if the user wakes up early to the first alarm at 3AM.
    The user will do tea, weather, and surfing.
    Then the program returns their updated points.
    
    """
    points += 10
    #proceed to the next activity: tea
    print("Good Job! You are awarded 10 points. It is tea time next!")
    
    tea = input("Would you like green tea, white tea, english breakfast, or earl grey?")
    print(f"Enjoy {tea}! Now you are fully awake!")

    #proceed to the next activity: check the weather
    weather = ["sunny", "windy", "rainy", "foggy", "stormy"]
    weather_today = random.choice(weather)
    temperature_today = random.randint(-10, 80)
    print(f"The weather today is {weather_today} and the temperature is {temperature_today} fahrenheit.")
   
    #proceed to the next activity: surfing
    points = surfing(points, weather_today)

    #update points earned so far
    return points


def wake_up_late(points):
    """
    Run the part of code that happens if the user snoozes the alarm and wakes up later.
    The user will be forced to wake up at 7AM.
    If the user wakes up before 7Am, they will study python. 
    At 7AM, the user will go to breakfast
    Then the program returns their updated points.

    """

    #user struggles to wake up. The alarm rings every hour until 7 AM.

    alarm = 3
    points -= 5
    print("You hit snooze and 5 points are deducted for everytime you snooze.")
    while alarm < 6:
        alarm += 1
        print(f"It is now {alarm}AM and alarm is ringing")
        get_up = input(f"Do you want noto get up at {alarm}AM? (yes/no): ").lower()
        if get_up == "no":
            points -= 5
            print("You hit snooze again.")
            #pause for 2 seconds to increase sense of reality
            time.sleep(2)
        else:
            print("Thank you for finally waking up! You will study python at Rhem Library until 7AM")
            break
    if alarm == 7:
        print("It is 7AM and the ear-screeching, catastrophic alarm forces you up!")
    
    #user proceed to breakfast
    time.sleep(2)
    print("Now that it is 7 AM, you are going to go to breakfast at Kimball")
    breakfast = input("You may choose from yogurt parfait, pancakes, bagels, and breakfast sandwich. What would you like?")
    print(f"{breakfast} is a good choice! You are awarded 5 points for nutrition intake!")
    points += 5

    return points


if get_up == "yes":
    points = wake_up_early(points)
else:
    points = wake_up_late(points)


def classes(points):
    """This block of code takes the user through the classes of the day."""
    print("It is now 8 a.m.. Time to finally start classes!!!")
    input("Are you excited?(yes/no):").lower()
    #this increases the user's participation rate. no response is returned.
    class_number = random.randint(1, 8)
    print(f"Bro, you have {class_number} classes today")

    #the student will be prompted that they are drowsy from waking up at 3a.m.
    drowsiness = input("You are experiencing a great heaviness in your head known as drowsiness from your alarm at 3AM. " 
    "Do you succumb to it and sleep in class?(yes/no):")
    if drowsiness == "yes":
        #If they chooses to sleep in class, their professors will hit them in the head with a chalk, “ouch”
        print("Ouch! Your professor throws a piece of chalk at you——wake up!")
        points -= 10    
    if drowsiness == "no":
        #If they chooses to fight drowsiness, they will take some mints.
        print("Good Student! Keep it up!")
        points += 15
    return points

points = classes(points)

def evening(points):
    """This block of the code takes the user through the evening: dinner, after-dinner, and bed"""
    print("You have succeeded through the day! Good effort!!!")
    time.sleep(2)
    print("You have survived through the academic day! Good effort!!")
    meet_friends = input("Would you like to meet up with apple, banana, and cherry for dinner at Crossroads? (yes/no): ")
    if meet_friends == "yes":
        points += 10
        print("Wonderful! Enjoy some time socializing!")
    else:
        print("Enjoy dinner all alone!")

    #proceed to after-dinner
    time.sleep(3)
    print("You will have some time to do homework, talk to your family, and unwind")
    
    #proceed to bed time
    time.sleep(3)
    print("It is 8 pm. Good night! You deserve to rest and restore!!")
    return points

points = evening(points)

#prints out the number of points earned and announces if the user wins or looses
print(f"Today you have scored {points} points!!!!! ")
if points < 0:
    print("You failed today. But tomorrow is a new day to do better!")
if points > 0:
    print("You succeeded today!! Yay!") 
elif points == 0:
    print("What a shame! You almost won the day!")