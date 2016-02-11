def convertToOrdinal(number=None):
    """This takes in a number, and converts it to an ordinal. Example, 1 gets converted to 1st, 2 gets convered to 2nd"""
    """This takes modulo of the number by 10 to get the last digit. It also takes modulo of 100 to get the last two digits. It then analyzes that information to come up with the ordinal output. It should be pretty straightforward"""
    ordinalNumber = None
    if number == None:
        number = int(input("Enter a number: "))
    numberModHundred = number % 100
    if numberModHundred >= 10 and numberModHundred <= 20:
        ordinalNumber = str(number) + 'th'
    else:
        onesColumnNumber = number % 10
        if onesColumnNumber == 1:
            ordinalNumber = str(number) + 'st'
        if onesColumnNumber == 2:
            ordinalNumber = str(number) + 'nd'
        if onesColumnNumber == 3:
            ordinalNumber = str(number) + 'rd'
        if ordinalNumber == None:
            ordinalNumber = str(number) + 'th'
    print(ordinalNumber)

convertToOrdinal()
