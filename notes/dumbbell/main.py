
# A workout builder by Stewart Engart

from csv import DictReader
import random
from datetime import datetime

DOY = datetime.now().timetuple().tm_yday
random.seed(DOY)
DAY = datetime.now().weekday()

def ab():
    choice = random.randint(0,2)
    print(f'{list_of_dict[choice]["Body Part"]} : {list_of_dict[choice]["Exercise"]}')

def back():
    choice = random.randint(3, 11)
    print(f'{list_of_dict[choice]["Body Part"]} : {list_of_dict[choice]["Exercise"]}')

def biceps():
    choice = random.randint(12, 29)
    print(f'{list_of_dict[choice]["Body Part"]} : {list_of_dict[choice]["Exercise"]}')

def chest():
    choice = random.randint(30, 38)
    print(f'{list_of_dict[choice]["Body Part"]} : {list_of_dict[choice]["Exercise"]}')

def forearms():
    choice = random.randint(39, 42)
    print(f'{list_of_dict[choice]["Body Part"]} : {list_of_dict[choice]["Exercise"]}')

def legs():
    choice = random.randint(43, 51)
    print(f'{list_of_dict[choice]["Body Part"]} : {list_of_dict[choice]["Exercise"]}')

def shoulders():
    choice = random.randint(52, 70)
    print(f'{list_of_dict[choice]["Body Part"]} : {list_of_dict[choice]["Exercise"]}')

def triceps():
    choice = random.randint(71, 77)
    print(f'{list_of_dict[choice]["Body Part"]} : {list_of_dict[choice]["Exercise"]}')

with open("stretch.csv", 'r') as f:
    dict_reader = DictReader(f)
    list_of_dict = list(dict_reader)
    print('# Stretch/Warmup')
    print('Neck Roll')
    for i in range(len(list_of_dict)):
        print(list_of_dict[i]["Neck Roll"])

with open("dumbbellExercises.csv", 'r') as f:
    dict_reader = DictReader(f)
    list_of_dict = list(dict_reader)
    match DAY:
        case 0:
            print(f'# Monday ({DOY}) Workout')
            print("## Chest and Triceps")
            legs()
            triceps()
            chest()
            back()
            triceps()
            biceps()
            forearms()
            chest()
            ab()
            triceps()
            chest()
        case 1:
            print(f"# Tuesday ({DOY}) Workout")
            print("## Back and Biceps")
            legs()
            back()
            biceps()
            ab()
            back()
            forearms()
            biceps()
            back()
            biceps()
        case 2:
            print(f"# Wednesday ({DOY}) Workout")
            print("## Legs and Abs")
            shoulders()
            legs()
            ab()
            chest()
            back()
            ab()
            legs()
            forearms()
            triceps()
            legs()
            ab()
        case 3:
            print(f"# Thursday ({DOY}) Workout")
            print("## Back and Shoulders")
            chest()
            back()
            shoulders()
            biceps()
            back()
            shoulders()
            forearms()
            back()
            shoulders()
            triceps()
        case 4:
            print(f"# Friday ({DO}) YWorkout")
            print("## Full Body")
            ab()
            back()
            biceps()
            chest()
            forearms()
            legs()
            shoulders()
            triceps()
        case _:
            print(f"REST DAY ({DOY})")
