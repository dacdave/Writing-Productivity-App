import datetime
from datetime import datetime, timedelta

goal = []

def insert(name, date, status):
    item = [date, name, status]
    goal.append(item)

def display_open():
    display = []
    for item in goal:
        if item[2] == False:
            display.append(item)
    print(f"\n**********\nThere are {len(display)} items in this To Do list.\n")
    for item in display:
        print(f"{item[0]}, {item[1]}, Not complete")
    print("**********")

def display_closed():
    display = []
    for item in goal:
        if item[2] == True:
            display.append(item)
    print(f"\n**********\nThere are {len(display)} items in this To Do list.\n")
    for item in display:
        print(f"{item[0]}, {item[1]}, Complete")
    print("**********")

def update_item():
    if len(goal) > 0:
        valid = False
        while valid == False:
            change = int(input("What would you like to do? (1: Change status; 2: Delete item) "))
            if change == 1:
                print("This functionality is not yet available. Please check back later.")
                valid = True
            elif change == 2:
                print("This functionality is not yet available. Please check back later.")
                valid = True
            else:
                print("Sorry, that's not a valid response. Please enter the number of your choice from the list.")
    else:
        print("There are no To Do items to update. Please add an item first.")

#text UI begins below
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