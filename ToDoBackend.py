import datetime
from datetime import datetime, timedelta
import json

goal = []

def insert(name, date, status):
    item = [date, name, status]
    goal.append(item)

def get_items(status):
    display = []
    if status == False:
        for item in goal:
            if item[2] == False:
                display.append(item)
    if status == True:
        for item in goal:
            if item[2] == True:
                display.append(item)
    return display

def sort_items():
    goal.sort(key=lambda x: x[0])
    return goal

def update(item, change, newvalue):
    task = goal[item]
    if change == 1:
        task[0] = newvalue
    elif change == 2:
        task[1] = newvalue
    elif change == 3:
        task[2] = newvalue

def delete(id):
    del goal[id]

#text UI begins below
def display_open():
    sort_items()
    todos = get_items(False)
    print(f"\n**********\nThere are {len(todos)} open items in this To Do list.\n")
    for item in todos:
        print(f"{item[0]}, {item[1]}, Not complete")
    print("**********")

def display_closed():
    sort_items()
    todos = get_items(True)
    print(f"\n**********\nThere are {len(todos)} complete items in this To Do list.\n")
    for item in todos:
        print(f"{item[0]}, {item[1]}, Complete")
    print("**********")

def update_item():
    if len(goal) > 0:
        valid = False
        while valid == False:
            change = int(input("1: Change status\n2: Delete item\nHow would you like to update the items? "))
            if change == 1:
                option = 0
                print("Which item would you like to change the status of?")
                while option < len(goal):
                    for item in goal:
                        if item[2] == False:
                            print(f"{option + 1}: {item[0]}, {item[1]}, Not complete")
                            option +=1
                        elif item[2] == True:
                            print(f"{option + 1}: {item[0]}, {item[1]}, Complete")
                            option +=1
                choice = int(input(">>> "))
                print(f"You chose item {choice} ({goal[choice - 1]}).")
                print(f"What would you like to change about {choice}?\n1. Due Date\n2. Description\n3. Completion Status")
                update_choice = int(input(">>> "))
                if update_choice == 1:
                    newdate = datetime.strptime(input("Please enter the new due date of the task (mm-dd-yyyy): "), "%m-%d-%Y").date()
                    newvalue = newdate
                elif update_choice == 2:
                    newdescription = input("Please enter the corrected description of the task: ")
                    newvalue = newdescription
                elif update_choice == 3:
                    newstatus = input("Is this task complete? (y/n) ")
                    if newstatus == "y" or "Y":
                        status = True
                    elif newstatus == "n" or "N":
                        status = False
                    newvalue = status
                update((choice - 1), update_choice, newvalue)
                valid = True
            elif change == 2:
                option = 0
                print("Which item would you like to delete?")
                while option < len(goal):
                    for item in goal:
                        if item[2] == False:
                            print(f"{option + 1}: {item[0]}, {item[1]}, Not complete")
                            option +=1
                        elif item[2] == True:
                            print(f"{option + 1}: {item[0]}, {item[1]}, Complete")
                            option +=1
                choice = int(input(">>> "))
                print(f"You chose item {choice} ({goal[choice - 1]}). This item will be deleted.")
                delete((choice - 1))
                valid = True
            else:
                print("Sorry, that's not a valid response. Please enter the number of your choice from the list.")
    else:
        print("There are no To Do items to update. Please add an item first.")

def collect():
    name = input("Please enter a description of the task: ")
    date = datetime.strptime(input("Please enter the due date of the task (mm-dd-yyyy): "), "%m-%d-%Y").date()
    status = False
    insert(name, date, status)

def main():
    if __name__ == "__main__":
        run = True
        while run == True:
            action = int(input("You may:\n1: Add Task\n2: Update Task\n3: View Complete Tasks\n4: View Open Tasks\n5: End Program\nWhat would you like to do? "))
            if action == 1:
                collect()
            elif action == 2:
                update_item()
            elif action == 3:
                display_closed()
            elif action  == 4:
                display_open()
            elif action == 5:
                run = False

main()