import os
from time import sleep
import json


def recipe_list():
    with open("cooking.json", "r") as openfile:
        recipe = json.load(openfile)
        recipe_list = str(recipe.keys())
        val = recipe_list.index("(")
        for i in recipe_list[val:]:
            print(i, end="")
        print()

cookbook = {}

home = '''
                                                                        .
                                                                      .....
                                                                    .........
                                                                      .....
                                                                      .....        
    '''

while True:
    print("                                          WELCOME TO UMAT COOKBOOK!!"
          "\n                                         WHAT ARE WE COOKING TODAY??")
    print("-------------------------------------------------------------------------------------------------------------------")
    print(home)
    print("enter 'help' to request command list\n")

    user = input("$:: ")
    user = user.capitcreatealize()

    if user == 'Help':
        print("'search' to search for recipe\n'create' to create recipe\n'exit' to leave cookbook")
        sleep(3)
        print("Returning.....")
        sleep(2)
        os.system('cls')

    elif user == "Search":
        print("enter 'full list' to request for full list of recipies")
        searching = input("Enter dish: ")
        searching = searching.capitalize()

        with open("cooking.json", 'r') as openfile:
            os.system("cls")
            recipe = json.load(openfile)
            try:
                if searching in recipe:
                    print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                    print(f":::::::::::::::::::::::::{searching}")
                    print(recipe[searching])
                    if input("$:: ") == "exit":
                        print("Returning....")
                        os.system("cls")
                elif searching == "Full list":
                    recipe_list()
                else:
                    print("\nRecipe doesnt exist T-T")
                    print("enter 'full list' to request for full list of recipies")
                    if input("$:: ") == "exit":
                        print("Returning....")
                        os.system("cls")
                    else:
                        recipe_list()
                        sleep(5)
                        print("Returning....")
                        sleep(1)
                        os.system('cls')
            except json.JSONDecodeError:
                print("\nRecipe doesnt exist T-T")                             
                print("enter 'full list' to request for full list of recipies")

    elif user == "Create":
        os.system("cls")
        print("\n@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@")
        print(":::::::::::::::::::::::::: READY TO CREATE NEW RECIPES :::::::::::::::::::::::::\n\n")
        title = input("COULD I KNOW THE NAME OF YOUR DISH??? \n$:: ")
        title = title.capitalize()
        print("\nenter 'end' to stop requesting for next step")
        print("enter 'exit' to leave to home")

        n = 0
        dish = ""
        while True:
            n += 1
            step = input(f"{n}.")
            if step == 'end':
                break
            dish += f"\n{n}.{step}"
        with open("cooking.json", "r") as openfile:
            recipe = json.load(openfile)
            recipe[title] = dish
        with open("cooking.json", "w") as outfile:
            json.dump(recipe, outfile, indent=4)

        if input("$:: ") == "exit":
            print("\n Returning.....")
            sleep(2)
            os.system('cls')
    elif user == "Exit":
        break