import random
import time
from surf_module import surfing
from user_validation import validation_for_yes_no, validation_for_choice, validation_for_int


print("Welcome to a day in the life of a holycross student")
points = 0
print("You start everyday with 0 points")
print("Good morning! It is 3 a.m. Your alarm is ringing...")

get_up = validation_for_yes_no("Did you get up on time? (yes/no): ")


def wake_up_early(points):
    """
    Run the part of code that happens if the user wakes up early to the first alarm at 3AM. The user will do tea, weather, and surfing.
    
    Input: points that represents current score.
    Output: points that represents updated score.
    Side effects: none.
    """
    points += 10
    #proceed to the next activity: tea
    print("Good Job! You are awarded 10 points. It is tea time next!")
    
    tea = validation_for_choice("Would you like green tea, white tea, english breakfast, or earl grey?",
                                ("green tea", "white tea", "english breakfast", "earl grey"))
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
    
    Input: points that represents current score.
    Output: points that represents updated score.
    Side effects: none
    """

    #user struggles to wake up. The alarm rings every hour until 7 AM.

    alarm = 3
    points -= 5
    print("You hit snooze and 5 points are deducted for everytime you snooze.")
    while alarm < 7:
        alarm += 1
        print(f"It is now {alarm}AM and alarm is ringing")
        get_up = validation_for_yes_no(f"Do you want noto get up at {alarm}AM? (yes/no): ")
        if get_up == "no":
            points -= 5
            print("You hit snooze again.")
            #pause for 2 seconds to increase sense of reality
            time.sleep(2)
        else:
            #if the user wakes up before 7Am, they will study python.
            print("Thank you for finally waking up! You will study python at Rhem Library until 7AM")
            break
    if alarm == 7:
        #the user will be forced to get up at 7AM
        print("It is 7AM and the ear-screeching, catastrophic alarm forces you up!")
    
    #user proceed to breakfast
    time.sleep(2)
    print("Now that it is 7 AM, you are going to go to breakfast at Kimball")
    breakfast = validation_for_choice("You may choose from yogurt parfait, pancakes, bagels, and breakfast sandwich. What would you like?",
                                      ("yogurt parfait", "pancakes", "bagels", "breakfast sandwich"))
    print(f"{breakfast} is a good choice! You are awarded 5 points for nutrition intake!")
    points += 5

    return points


if get_up == "yes":
    points = wake_up_early(points)
else:
    points = wake_up_late(points)


def classes(points):
    """
    This block of code takes the user through the classes of the day.
    
    Input: points that represents current score.
    Output: points that represents updated score.
    Side effects: none
    """
    time.sleep(3)
    print("It is now 8 a.m.. Time to finally start classes!!!")
    validation_for_yes_no("Are you excited?(yes/no):")
    #this increases the user's participation rate. no response is returned.
    class_number = random.randint(1, 8)
    print(f"Bro, you have {class_number} classes today")

    #the student will be prompted that they are drowsy from waking up at 3a.m.
    drowsiness = validation_for_yes_no("You are experiencing a great heaviness in your head known as drowsiness from your alarm at 3AM. " 
    "Do you succumb to it and sleep in class?(yes/no):")
    if drowsiness == "yes":
        #If they chooses to sleep in class, their professors will hit them in the head with a chalk, “ouch”
        print("Ouch! Your professor throws a piece of chalk at you——wake up!")
        points -= 10    
        time.sleep(3)
        print("You will try to stay alert better")
    if drowsiness == "no":
        #If they chooses to fight drowsiness, they will take some mints.
        print("Good Student! Keep it up!")
        points += 15
    return points

points = classes(points)

def evening(points):
    """
    This block of the code takes the user through the evening: dinner, after-dinner, and bed.
    
    Input: points that represents current score.
    Output: points that represents updated score.
    Side effects: none
    """
    time.sleep(2)
    print("Now all classes are over. You have survived through the day! Good effort!!!")
    print("You have survived through the academic day! Good effort!!")
    meet_friends = validation_for_yes_no("Would you like to meet up with apple, banana, and cherry for dinner at Crossroads? (yes/no): ")
    if meet_friends == "yes":
        points += 10
        print("Wonderful! Enjoy some time socializing!")
    else:
        print("Enjoy dinner all alone!")

    #proceed to after-dinner
    time.sleep(2)
    evening_activity = validation_for_choice("In the evening you will have some time to do homework, talk to your family, and unwind. Which do you choose?", 
                                             ("do homework", "talk to family", "unwind"))
    
    #proceed to bed time
    time.sleep(3)
    print("It is 8 pm. Good night! You deserve to rest and restore!!")
    return points

points = evening(points)


def win_loss_announcement(points):
    """
    This function prints out the number of points earned and announces if the user wins or looses.

    Input: the global variable points
    Output: printed words
    Side effects: none
    """
    print(f"Today you have scored {points} points!!!!! ")
    if points < 0:
        print("You failed today. But tomorrow is a new day to do better!")
    if points > 0:
        print("You succeeded and won today!! Yay!") 
    elif points == 0:
        print("What a shame! You almost won the day!")

if __name__ == "__main__":
    win_loss_announcement(points)