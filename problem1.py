#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""

people = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
pos = None

def remove():
    global pos
    print(people)
    rem = str(input("Choose a person from the list to replace: "))
    if rem in people:
        pos = people.index(rem)
        people.pop(pos)
        return
    else:
        print("Invalid input")
        remove()

def replace():
    global pos
    rep = str(input("Enter the replacement: "))
    people.insert(pos, rep)

def ask():
    remove()
    replace()
    print(people)

ask()