TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

#Prihlaseni uzivatele: overeni uzivatelskeho jmena a hesla.
username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username in users and password in users.get(username):
    print(f"username: {username}", f"password: {password}", "-"*40, 
          f"Welcome to the app, {username}", 
          f"We have 3 texts to be analyzed.", "-"*40, sep="\n")
    text_number = input("Enter a number btw. 1 and 3 to select: ")
    #Ocislovani textu.
    list(enumerate(TEXTS, start = 1))
    #Overeni, ze uzivatel zadal platnou hodnotu (cislo textu) a ze je v rozsahu 1-3.
    if text_number.isdigit():
        number = int(text_number)
        if 1 <= number <= len(TEXTS):
            text = TEXTS[number - 1]
            print("ANALYSED TEXT: ")
            print(text)
            print("-"*40) 
            
            #Zacatek analyzy textu.
            #Pocet slov v textu.
            total_words = len(text.split())
            print(f"There are {total_words} words in the selected text.")

            #Pocet slov zacinajicich velkym pismenem.
            titlecase_words = [word for word in text.split() if word.istitle()]
            print(f"There are {len(titlecase_words)} titlecase words.")

            #Pocet slov psanych velkymi pismeny.
            uppercase_words = [word for word in text.split() if word.isupper()]
            print(f"There are {len(uppercase_words)} uppercase words.")

            #Pocet slov psanych malymi pismeny.
            lowercase_words = [word for word in text.split() if word.islower()]
            print(f"There are {len(lowercase_words)} lowercase words.")

            #Pocet cisel, ne cifer.
            numbers_in_text = [word for word in text.split() if word.strip(".,;!?:").isnumeric()]
            print(f"There are {len(numbers_in_text)} numeric strings.")

            #Soucet vsech cisel (ne cifer) ve vybranem textu.
            numbers_sum = [int(number) for number in numbers_in_text]
            print(f"The sum of all the numbers {sum(numbers_sum)}")

            print("-"*40, "LEN|     OCCURENCES     |NR.", "-"*40, sep="\n")

            #Graficke zobrazeni (sloupcovy graf) cetnosti ruznych delek slov.
            occurence = dict()

            for word in text.split():
                word = word.strip(".,;!?")
                words_len = len(word) #Delka jednotlivych slov.
                if words_len in occurence: #Naplneni slovniku "occurence" poctem jednotlivych delek slov.
                    occurence[words_len] += 1
                else:
                    occurence[words_len] = 1
            for key, value in sorted(occurence.items()):
                print(f"{key:>3}|{"*" * value:<20}|{value}")

        else: 
            print("Entered wrong number, terminating the program..")
    else: 
        print("Entered value, not number, terminating the program..")
else:
    print(f"username: {username}", f"password: {password}", 
          "unregistered user, terminating the program..", sep="\n")
    