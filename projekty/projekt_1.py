##############################################################################

'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Schuster
email: schuster.jan@seznam.cz
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive
topographic feature that rises sharply some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet above sea level. The butte is located 
just north of US 30N and the Union Pacific Railroad, which traverse the valley. 
''',
'''At the base of Fossil Butte are the bright red, purple, yellow and gray beds 
of the Wasatch Formation. Eroded portions of these horizontal beds slope 
gradually upward from the valley floor and steepen abruptly. Overlying them and 
extending to the top of the butte are the much steeper buff-to-white beds of 
the Green River Formation, which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects a portion of the largest 
deposit of freshwater fish fossils in the world. The richest fossil fish 
deposits are found in multiple limestone layers, which lie some 100 feet below 
the top of the butte. The fossils represent several varieties of perch, as well 
as other freshwater genera and herring similar to those in modern oceans. 
Other fish such as paddlefish, garpike and stingray are also present.''']

# define dictionary to store active users with permissions to enter the program
users = {
    'bob' : '123',
    'ann' : 'pass123',
    'mike' : 'password123',
    'liz' : 'pass123',
}

# store the length of the list where the texts are stored
num_of_texts = len(TEXTS)

# ask for the credentials username first and then password
username = input("username: ")
password = input("password: ")

# check if the user does exist in the dictionary, if not exit the program
if users.get(username) != password:
    print(f"username:{username}")
    print(f"password:{password}")
    print("unregistered user, terminating the program..")

# start the program in case user has entered valid credentials
else:
    # say hello to the user and ask him which text should be analyzed (input)
    print("-" * 40)
    print(f"Welcome to the app, {username}")
    print(f"We have {num_of_texts} texts to be analyzed.")
    print("-" * 40)
    num_selection = input(f"Enter a number btw. 1 and {num_of_texts} "
                          "to select: ")
    print("-" * 40)
    
    # check if the input is an integer - in case it is not stop the program
    if num_selection.isdigit() is False:
        print("You should have selected integer. I am closing the program.")

    # check if the given integer is in the required range 
    # - in case it is not stop the program
    elif int(num_selection) not in range(1, num_of_texts + 1):
        print("You should have selected integer from the given range."
              " I am closing the program.")
    
    # the input was given correctly, we can start the program itself
    else:
        # convert the user's input to integer 
        num_selection = int(num_selection)

        # list to store words followed by loop storing clean words in it
        # indexes in the texts list start with 0, therefore num_selection - 1
        cleaned_up_words = []
        for word in TEXTS[num_selection - 1].split(): 
            clean_word = word.strip('.,<>?!"')
            cleaned_up_words.append(clean_word)

        # helpful dictionary to store number of words with specific 
        # number of letters. The range can be extended if necessary
        numbers_of_letters = {}
        for num in range(1,21):
            numbers_of_letters[num] = 0

        # declared variables to store requested information
        number_of_words = 0
        titlecase_words = 0
        uppercase_words = 0
        lowercase_words = 0
        numeric_strings = 0
        sum_of_nums = 0

        # the code to store requested information in the variables
        for word in cleaned_up_words:
            #operations on both strings and numbers 
            number_of_words += 1
            numbers_of_letters[len(word)] += 1

            # operations on numbers, we don't have to deal with the float 
            # data type, because we have removed dots while cleaning the text
            if word.isdigit():
                numeric_strings += 1
                sum_of_nums += int(word)

            # operations on strings
            # something is a bit unclear to me - such as how to deal with '30N'
            # - it is both titlecase and uppercase. In case it would have to be 
            # counted in both, there would be no elifs, only ifs
            else:
                if word.istitle():
                    titlecase_words += 1
                elif word.isupper():
                    uppercase_words += 1
                elif word.islower():
                    lowercase_words += 1

        # printing the final result to the user
        print(f"There are {number_of_words} words in the selected text.")
        print(f"There are {titlecase_words} titlecase words.")
        print(f"There are {uppercase_words} uppercase words.")
        print(f"There are {lowercase_words} lowercase words.")
        print(f"There are {numeric_strings} numeric strings.")
        print(f"The sum of all the numbers {sum_of_nums}")
        print("-" * 40)
        print(f"LEN|{' ' * 2}OCCURENCES{' ' * 2}|NR.")
        print("-" * 40)    
        for num, value in numbers_of_letters.items():
            if value > 0:
                print(f"{num :> 3}|{'*' * (13 if value > 13 else value)}"
                      f"{' ' * (14 - (13 if value > 13 else value))}|{value}")

##############################################################################

