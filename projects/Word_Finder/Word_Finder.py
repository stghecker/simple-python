while True:

    words = input("Paste or write your text here: \n") #gets users text
    char = input("Write the character you want to find here: \n") #asks user to specify what charracter program should look for
    count = words.count(char) #main function that calculates how many times a specific character appears in users text

    print("\n==============================================\n" \
         f"The character '{char}' appears {count} times.\n"
         "==============================================\n")

#STGHECKER#
#Hard2Recall# Fixed code structure, cleaned print function, added my signature