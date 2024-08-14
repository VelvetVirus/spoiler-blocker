# takes a dictonary from the user to block
# the user try to enter a sentance, if a sentance containing spolier it will get stared and stored
# the programm would ask user whether or not if they wanted a add/edit/delete/exitprogram

import sys
import json

# SPOLIER = []

try:
    with open("./censored.json", "r") as censored:
        SPOLIER = json.load(censored)
        print("exists, reading:", SPOLIER)

except FileNotFoundError:
    SPOLIER = []
    with open("./censored.json", "w") as censored:
        json.dump(SPOLIER, censored, indent=4)
        print("File does not exist, \n creating and initializing with an empty dictionary. \n" + "#" * 10)

STATE = True

print("hey, this is a spoiler blocker, simply put: an input would appear and asks you to put a word you'd like to block \
      \n You can add/edit/delete/view/test/exit this program \
      \n do not worry, this program stores the input in a json file")
    
while STATE:
    userChoice = input("what would you like to do? (add/edit/delete/view/test/exit) ").strip().lower()

    if userChoice == "exit":
        sys.exit()
    
    elif userChoice == "add":
        word_to_add = input("What would you like to add? ").strip().lower()
        SPOLIER[word_to_add] = word_to_add  # Add the word to the dictionary
        with open("./censored.json", "w") as censored:
            json.dump(SPOLIER, censored, indent=4)
        print(f"Added '{word_to_add}' to the list.")

    elif userChoice == "edit":
        with open("./censored.json", "r") as censored:
            SPOLIER = json.load(censored)
        print("This is your word list:\n", SPOLIER)
        old_word = input("What would you like to edit? (type out the word) ").strip().lower()
        if old_word in SPOLIER:
            new_word = input("What would you like to change it to? ").strip().lower()
            SPOLIER[new_word] = SPOLIER.pop(old_word)  # Change the word
            with open("./censored.json", "w") as censored:
                json.dump(SPOLIER, censored, indent=4)
            print(f"Edited '{old_word}' to '{new_word}'.")
        else:
            print(f"'{old_word}' does not exist in the list.")

    elif userChoice == "view":
        with open("./censored.json", "r") as censored:
            SPOLIER = json.load(censored)
            print("Current list of words to block:\n", SPOLIER)

    elif userChoice == "delete":
        word_to_delete = input("What would you like to delete? (type the word) ").strip().lower()
        if word_to_delete in SPOLIER:
            del SPOLIER[word_to_delete]  # Delete the word
            with open("./censored.json", "w") as censored:
                json.dump(SPOLIER, censored, indent=4)
            print(f"Deleted '{word_to_delete}'.")
        else:
            print(f"'{word_to_delete}' does not exist in the list.")

    elif userChoice == "test":
        test_case = input("input what would you like to type, the program would \
        make the words in the spoiler file change with a star '*': ")
        test_case_lower = test_case.lower()
        cleared_sentence = ""
        for word in test_case_lower.split():
            if word not in SPOLIER:
                cleared_sentence += word + " "
            else: cleared_sentence += "*" + " "
        print("here is your test case: " + cleared_sentence.rstrip())

    else:
        print("***** Input error, try to type the command correctly *****")