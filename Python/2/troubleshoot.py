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

# Define a dictionary containing all the solutions for the keywords
keywords = {
    'smashed'      : 'Please take your phone to the nearest repair shop',
    'charging'     : 'Try cleaning out your charging port on your phone by blowing into it',
    'screen'       : 'Please take your phone to the nearest repair shop',
    'wet'          : 'Please take your phone to the nearest repair shop',
    'water'        : 'Please take your phone to the nearest repair shop',
    'slow'         : 'You may need to upgrade your phone',
    'audio'        : 'Try hard resetting your phone',
    'sound'        : 'Try hard resetting your phone',
    'home'  : 'Please take your phone to the nearest repair shop'
}

print "Welcome to James' troubleshooting program."
# Set a variable called 'loops' to 0, used to track how many times the user has typed an issue
loops = 0
# Loop the contained code segment whilst the 'loops' variable is less than or equal to 1
# -- This esentially only lets the user have 2 attempts with their question --
while loops <= 1:
    # Ask the user what their issue is, take their answer, convert it to lowercase and store in the 'issue' variable
    issue = sysinp('What is your issue?').lower()
    # If the user's input is blank
    if issue.strip() == '':
        # Then exit and tell them their input is incorrect
        incorrect_answer()
    # Else
    else:
        # Split the words in the 'issue' variable into an array called 'words'
        words = issue.split()
        # Declare an empty array, used for logging the keyword matches within the users issue
        matches = []
        # Loop over each item in the 'words' array and make it accesible as the variable 'word'
        for word in words:
            # If the 'word' variable exists as a key in the 'keywords' dictionary
            if word in keywords:
                # Then add the current word into the 'matches' array
                matches.append(word)
            # Else
            else:
                # Move on
                continue
        # If there's more than 0 items in the 'matches' array
        if len(matches) > 0:
            # Then give the user the solution related to their key word, wish them luck and exit
            solution(keywords[matches[0]])
        # Else
        else:
            # If it's only the first loop
            if loops == 0:
                # Then tell them to try again
                sysp('Sorry, we do not have a solution for the given issue, please try again.')
            # Else (they've had 2 attempts)
            else:
                # Break out of the loop moving them onto the catching line at the bottom which tells them there's no solution and ends the program
                break
            # Increment the 'loops' variable by 1
            loops += 1

# Tell the user there's no solution
sysp('Sorry, we could not find a solution for you.')
