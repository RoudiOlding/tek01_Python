'''
2. Temperature converter
-- Create a program that converts Celsius to Fahrenheit or vice versa based on the user’s choice.
-- Concepts: type casting, conditionals, input
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