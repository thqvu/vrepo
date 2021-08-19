'''
first_str = "Hello"
second_str = "World"
third_str = "from Vu"
print(first_str, second_str, third_str, sep=",", end=".")
third_str = "A single quoted literal string with an \' escaped single quote"
fourth_str = "A double quoted literal string with a \" double quote"
fifth_str = "A literal string with a \n new line character"
sixth_str = "A literal string with a \t tab character"
print(third_str)
print(fourth_str)
print(fifth_str)
print(sixth_str)
seventh_str = r"A literal string with a \n new line charcter printed raw"
print(seventh_str)
'''
medicine = "Coughussin"
dosage = 5
duration = 4.5
instructions = "{} - Take {} ML by mouth every {} hours".format(medicine, dosage, duration)
print(instructions)

instructions = "{2} - Take {1} ML by mouth every {0} hours".format(medicine, dosage, duration)
print(instructions)

instructions = "{medicine} - Take {dosage} ML by mouth every {duration} hours".format(medicine = "Sneezergen", dosage = 10, duration = 6)
print(instructions)