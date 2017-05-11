# Function for printing a message with the [System] prefix
def sysp (msg):
    print ("\n[System]: "+msg+"")

# Function for requesting user input with the [System] prefix
def sysinp (msg):
    return raw_input("\n[System]: "+msg+": ")

# Function for telling the user their answer was incorrect and exiting the program
def incorrect_answer ():
    sysp('Incorrect answer! Exiting...')
    exit()

# Function for printing a solution, wishing the user good luck and exiting
def solution (msg):
    sysp('Solution: '+msg)
    print "\n\n Good luck!"
    exit()

print "Welcome to James' troubleshooting program."
# Reqest the user's name & store it in the 'name' variable
name = sysinp("Please enter your name: ")
# Greet the user
sysp("Hello, "+name)

# Ask the user if their phone has gotten very wet, take their answer, convert it to lowercase and store in the 'phone_very_wet' variable
phone_very_wet = sysinp("Has your phone gotten very wet? (y/n)").lower()
# If the user typed 'y'
if phone_very_wet == 'y':
    # Then tell them to take their phone to the repair shop
    solution('Please take your phone to the nearest repair shop!')
# Else if the user typed 'n'
elif phone_very_wet == 'n':
    # Ask the user if their phone has gotten wet at all, take their answer, convert it to lowercase and store in the 'phone_wet' variable
    phone_wet = sysinp("Has your phone gotten wet at all? (y/n)").lower()
    # If the user typed 'y'
    if phone_wet == 'y':
        # Then tell them to try leaving their phone in a bowl of dry rice overnight
        solution('Please try leaving your phone in a bowl of dry rice overnight!')
    # Else if the user typer 'n'
    elif phone_wet == 'n':
        # Move on
        pass
    else:
        # Their answer wasn't 'y' or 'n', tell them it's an incorrect answer and exit via the incorrect_answer() function
        incorrect_answer()
# Else
else:
    # Their answer wasn't 'y' or 'n', tell them it's an incorrect answer and exit via the incorrect_answer() function
    incorrect_answer()

# Ask the user if their phone is running very slowly, take their answer, convert it to lowercase and store in the 'phone_slow' variable
phone_slow = sysinp("Is your phone running very slowly? (y/n)").lower()
# If the user typed 'y'
if phone_slow == 'y':
    # Then ask the user if their phone model is more than 3 years old, take their answer, convert it to lowercase and store in the 'phone_old' variable
    phone_old = sysinp('Is your phone model more than 3 years old? (y/n)').lower()
    # If the user typed 'y'
    if phone_old == 'y':
        # Then tell them to upgrade their phone to a newer model
        solution("Upgrade your phone to a newer model!")
    # Else if the user typed 'n'
    elif phone_old == 'n':
        # Then tell them to conduct a hard reset on their phone
        solution("Conduct a hard reset on your phone!")
    # Else
    else:
        # Their answer wasn't 'y' or 'n', tell them it's an incorrect answer and exit via the incorrect_answer() function
        incorrect_answer()
# Else if the user typed 'n'
elif phone_slow == 'n':
    # Move on
    pass
# Else
else:
    # Their answer wasn't 'y' or 'n', tell them it's an incorrect answer and exit via the incorrect_answer() function
    incorrect_answer()

# Ask the user if their phone screen is smashed, take their answer, convert it to lowercase and store in the 'phone_smashed' variable
phone_smashed = sysinp("Has your phone screen smashed? (y/n)").lower()
# If the user typed 'y'
if phone_smashed == 'y':
    # Then tell them to take their phone to the nearest repair shop
    solution('Please take your phone to the nearest repair shop!')
# Else if the user typed 'n'
elif phone_smashed == 'n':
    # Move on
    pass
# Else
else:
    # Their answer wasn't 'y' or 'n', tell them it's an incorrect answer and exit via the incorrect_answer() function
    incorrect_answer()

# Ask the user if their phone is failing to charge, take their answer, convert it to lowercase and store in the 'phone_wont_charge' variable
phone_wont_charge = sysinp("Is your phone failing to charge? (y/n)").lower()
# If the user typed 'y'
if phone_wont_charge == 'y':
    # Then tell them to clean out their charging port
    solution('Please clean out the charging port on your phone by blowing hard into it!')
# Else if the user typed 'n'
elif phone_wont_charge == 'n':
    # Move on
    pass
# Else
else:
    # Their answer wasn't 'y' or 'n', tell them it's an incorrect answer and exit via the incorrect_answer() function
    incorrect_answer()

# Ask the user if their phone is lost, take their answer, convert it to lowercase and store in the 'phone_lost' variable
phone_lost = sysinp("Is your phone lost? (y/n)").lower()
# If the user typed 'y'
if phone_lost == 'y':
    # Then tell them to contact their phone provider
    solution('Please contact your phone provider!')
# Else if the user typed 'n'
elif phone_lost == 'n':
    # Move on
    pass
# Else
else:
    # Their answer wasn't 'y' or 'n', tell them it's an incorrect answer and exit via the incorrect_answer() function
    incorrect_answer()

# Ask the user if their phone is turning off at random percentages, take their answer, convert it to lowercase and store in the 'phone_battery_issues' variable
phone_battery_issues = sysinp("Is your phone turning off at random battery percentages? (y/n)").lower()
# If the user typed 'y'
if phone_battery_issues == 'y':
    # Ask the user if their phone is runnion iOS 10 or above, take their answer, convert it to lowercase and store in the 'iosten' variable
    iosten = sysinp("Is your phone running iOS 10 or above? (y/n)").lower()
    # If the user typed 'y'
    if iosten == 'y':
        # Ask the user if their phone is updated to the most recent version, take their answer, convert it to lowercase and store in the 'updated' variable
        updated = sysinp("Is your phone updated to the most recent version? (y/n)").lower()
        # If the user typed 'y'
        if updated == 'y':
            # Then tell them to take their phone to the nearest repair shop
            solution('Please take your phone to the nearest repair shop!')
        # Else if the user typed 'n'
        elif updated == 'n':
            # Then tell them to update to the most recent version
            solution('Please update to the most recent version!')
        # Else
        else:
            # Their answer wasn't 'y' or 'n', tell them it's an incorrect answer and exit via the incorrect_answer() function
            incorrect_answer()
    # Else if the user typed 'n'
    elif iosten == 'n':
        # Then tell them to take their phone to the nearest repair shop
        solution('Please take your phone to the nearest repair shop!')
    # Else
    else:
        # Their answer wasn't 'y' or 'n', tell them it's an incorrect answer and exit via the incorrect_answer() function
        incorrect_answer()
# Else if the user typed 'n'
elif phone_battery_issues == 'n':
    # Move on
    pass
# Else
else:
    # Their answer wasn't 'y' or 'n', tell them it's an incorrect answer and exit via the incorrect_answer() function
    incorrect_answer()

# We have no solutions, tell them to take their phone to the nearest repair shop
solution('Please take your phone to the nearest repair shop!')
