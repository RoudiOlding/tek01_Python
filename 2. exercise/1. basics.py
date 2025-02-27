## EASY LEVEL

'''
1. Sum of Even Numbers
-- Write a program that asks the user for a positive integer and sums all even numbers from 1 up to that number.
-- Concepts: loops, conditionals, variables.
'''

'''
print('Hello to exercise 1')
number = int(input('Please, give a number: '))
sum = 0

for x in range(number+1):
    if((x%2) == 0):
        sum+= x

print(f'Youre original number was {number}, and the sum of even numbers is {sum}')

'''


'''
2. Temperature converter
-- Create a program that converts Celsius to Fahrenheit or vice versa based on the user’s choice.
-- Concepts: type casting, conditionals, input
'''

'''
def convertTemperature(foption, ftemp):
    convert = 0
    if foption == 1:
        convert = (ftemp - 32) * 5/9
        print (convert)
    else:
        convert = (ftemp * 9/5) + 32
        print(convert)


def userInput():
    option = int(input('1. Convert to Celcius' + '\n' + '2. Convert to Fahrenheit' + '\n' + '...'))
    while (option != 1) and (option != 2):
        option = int(input('Try again' + '\n' + '1. Convert to Celcius' + '\n' + '2. Convert to Fahrenheit' + '\n' + '...'))
    
    tempe = float(input('Enter the temperature: '))

    return option, tempe

if __name__ == "__main__":
    print('Welcome to exercise 2')
    foption, ftempe = userInput()
    convertTemperature(foption, ftempe)
''' 

'''
3. Voul counter
-- Ask the user for a word and count how many vowels it contains.
-- Concepts: loops, conditionals, lists.
'''

'''
def checkVowels(fword):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    for letter in fword:
        for i in range(len(vowels)):
            if letter == vowels[i]:
                counter+= 1

    return counter

if __name__ == "__main__":
    print('Welcome to exercise 3')
    word = input('Give me a word: ')
    nVowels = checkVowels(word)
    print(f'Your word {word}, have {nVowels}')

'''

## INTERMEDIUM LEVEL

'''
4. Password validator
-- Build a program that checks if a password is valid based on these rules:
    . At least 8 characters.
    . Contains at least one uppercase letter, one lowercase letter, and one number.
-- Concepts: conditionals, loops, functions, type casting.


def checkPassword():
    while True:
        passw = input('Create a password (it must contain)\n'
                    '1. At least 8 characters\n'
                    '2. At least one uppercase letter\n'
                    '3. One lowercase letter\n'
                    '4. One number\n'
                    '...: ')
        
        # Check conditions
        has_upper = any(char.isupper() for char in passw)  # ANY checks if At least one uppercase letter
        has_lower = any(char.islower() for char in passw)  # ANY checks if At least one lowercase letter
        has_digit = any(char.isdigit() for char in passw)  # ANY checks if At least one number
        has_length = len(passw) >= 8  # At least 8 characters

        # If all conditions are met, exit the loop
        if has_upper and has_lower and has_digit and has_length:
            print('Your password is valid!')
            return passw
        else:
            print('Your password is not valid. Please try again.\n')

if __name__ == "__main__":
    print('Welcome to exercise 4')
    checkPassword()

'''

'''
5. Contact Book
-- Create a program that allows users to:
    . Add contacts with name and phone number.
    . View all contacts.
    . Search for a contact by name.
-- Concepts: Dictionaries, Functions, Loops

def addContact(fbook, fname, fnumber):
    fbook['name'].append(fname)
    fbook['phone'].append(fnumber)
    print(f'Name: {fname} with number {fnumber}... Add sucessfully!')

def viewAllContacts(fcontact):
    if not fcontact['name']:  # Check if the 'name' list is empty
        print('You don\'t have any contacts yet!')
    else:
        for i in range(len(fcontact['name'])):
            print(f"Contact {i + 1}. -- Name: {fcontact['name'][i]}, Phone: {fcontact['phone'][i]}")

def searchContact(fcontact, fname):
    for i in range(len(fcontact['name'])):
        if(fcontact['name'][i] == fname):
            print(f"Heres your contact. Name: {fcontact['name'][i]}, Phone: {fcontact['phone'][i]}")

if __name__ == "__main__":
    # Contact book default
    contactBook = {
        'name': [],
        'phone': [],
    }
    print('Welcome to exercise 5')
    
    option = 1
    while option != 4:
        option = int(input('Choose an option: \n' + '1. Add contact\n' + '2. View all contacts\n' + '3. Search contact\n' + '4. Exit\n'))
        if option==1:
            fname = input('Name: ')
            fphone = input('Phone: ')
            addContact(contactBook, fname, fphone)
        elif option==2:
            viewAllContacts(contactBook)
        elif option==3:
            searchContact(contactBook, fname = input('Give me the name: '))
        elif option == 4:
            print('Goodbye')
            option = 4
        else:
            print('Invalid option, try again!\n')

'''

'''
6. Calculator with Error Handling:
-- Build a basic calculator that performs addition, substraction, multiplication and division.
-- Implement exception handling to avoid errors like diving zero or invalid inputs.
-- Concepts: functions, exceptions, conditionals


def addOp(fx, fy):
    print(f"Result: {fx + fy}\n")

def subdOp(fx, fy):
    print(f"Result: {fx - fy}\n")

def multiOp(fx, fy):
    print(f"Result: {fx * fy}\n")

def divOp(fx, fy):
        try:
            print(f"Result: {fx / fy}\n")
            
        except ZeroDivisionError:
            print("You can't divide by zero")


if __name__ == "__main__":
    print("Welcome to exercise 6")
    option = 0
    while option != 5:
        option = int(input('Choose an option: \n' + '1. Add\n' + '2. Sub\n' + '3. Multi\n' + '4. Divisi\n' + '5. Exit\n'))
        if option==1:
            x = float(input('Number 1: '))
            y = float(input('Number 2: '))
            addOp(x, y)
        elif option==2:
            x = float(input('Number 1: '))
            y = float(input('Number 2: '))
            subdOp(x, y)
        elif option==3:
            x = float(input('Number 1: '))
            y = float(input('Number 2: '))
            multiOp(x, y)
        elif option==4:
            x = float(input('Number 1: '))
            y = float(input('Number 2: '))
            divOp(x, y)
        elif option==5:
            print('Goodbye')
            option = 5
        else:
            print('Invalid option, try again!\n')
'''

## HARD
'''
7. To-do List Manager
-- Create a program that lets users:
	•	Add tasks.
	•	Mark tasks as completed.
	•	Delete tasks.
	•	View pending and completed tasks.
-- Use lists and dictionaries to manage tasks and their statuses.
-- Include error handling (e.g., trying to complete a non-existing task).
-- Concepts: lists, dictionaries, functions, exceptions, loops.
'''