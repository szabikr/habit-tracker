import sys
from logging_config import setup_logging
setup_logging()

db_file_name = 'data.txt'

from import_activities import import_activities
from when_did_i_do import when_did_i_do

def print_divider(divider=" "):
    print(divider * 5)

def get_menu_item():
    while True:
        print_divider()
        print("Menu")
        print("1. Import user input from file")
        print("2. Find out when did you do an activity")
        print("0. Exit")
        menu_item = input("Enter a menu item number:\n")
        if menu_item in ["0", "1", "2"]:
            return menu_item
        print("Sorry, I don't yet know how to do that. Try again")
        print_divider("-")

if __name__ == '__main__':
    print("Welcome to your personal habit tracker!")
    print_divider("=")
    while True:
        menu_item = get_menu_item()
        if menu_item == "0":
            print_divider()
            print("See you soon!")
            sys.exit()
        
        elif menu_item == "1":
            print_divider()
            print("Import user input from file")
            print_divider("-")
            file_name = "user_input/" + input("Enter file name:\n")
            activities_count = import_activities(file_name, db_file_name)
            print(f"You just imported {activities_count} activities")

        elif menu_item == "2":
            print_divider()
            print("Find out when did you do an activity")
            print_divider("-")
            activity_name = input("Enter activity name:\n")
            when_did_i_do(activity_name, db_file_name)
