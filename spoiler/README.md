# Spoiler Blocker
- hello, this is a program of a spoiler blocker, and this is how to use it and then I'll show you how it's constructed


## Introduction:
- this is a program to hide any words in the json file, it will replace it with a star `*` instead of the actual word

---

### How to use:
This program will run in a loop asking you for five simple commands:
- add: this will add words to your spoiler list
- edit: this will make you edit the words you want to change, without the need to delete and add a new word
- delete: this will make you delete the words you'd want to delete
- view: this will make you view the list of words you put
- test: this will take an input from you and give you the sentance/word/test case and print it out without the word you wanted to remove
- exit: will exit the program

## requirments:
python 3.6 or older

## How does this code works?
this code runs on python, it creates a dictonary list in json file (it will check whether json file of the dictonary list does exist or not) and then make a while loop containing all the commands, it will also make a for loop in the test case to check that there isn't a word in the dictonary then it will print out the word.