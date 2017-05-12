import os
import time as t

# Function for printing a message with the [System] prefix
def sysp (msg):
    print ("\n[System]: "+msg+"")

# Function for check if a variable is blank
def check_blank (var):
    if (var.strip() == ''):
        sysp('Illegal input! Exiting')
        exit()
        return 1
    else:
        return 0

# Function for requesting user input with the [System] prefix
def sysinp (msg):
    input = raw_input("\n[System]: "+msg+": ")
    check_blank(input)
    return input;

print "Welcome to James' troubleshooting program."
# Ask the user what device they are having issues with, take their answer, put it in lowercase and store it in a variable called 'device'
device = sysinp('What device are you having issues with?').lower()
# Ask the user what model their phone is, take their answer, put it in lowercase and store it in a variable called 'model'
model = sysinp('What model is it?').lower()
# Concatenate the device input, model input and .txt to form the filename to look for
filename = device + model + '.txt'
# If it exists
if(os.path.exists(filename)):
    # Then ask the user what their issue is, take their answer, put it in lowercase and store it in a variable called 'issue'
    issue = sysinp('What is your issue?').lower()
    # Open the file and make it accesible via the 'solutions' variable
    with open(filename,'r') as solutions:
        # Loop over each line
        for solution in solutions:
            # If the user's issue appears in the line
            if issue in solution:
                # Then set 'finalSolution' to a newline stripped version of the second element in the array produced by splitting the line at the ':' character
                finalSolution = solution.split(':')[1].rstrip()
                # Print the solution
                sysp('Solution: '+finalSolution)
                # Exit the program
                exit()
                # Break the loop
                break
            # Else
            else:
                # Move on
                continue
        # Tell the user there's no solution
        sysp('Sorry but we do not have a solution for you. We will log your issue with a case number for our agents to look at.')
        # Set the 'case_number' variable to the current unix timestamp typecasted to an integer
        case_number = str(int(t.time()))
        # Make a case .txt file called case-CASE_NUMBER.txt and make it accesible via the 'case' variable
        case = open('case-'+case_number+'.txt', 'w+')
        # Write the case number at the top of the file
        case.write('Case number: '+case_number+'\n\n')
        # Write the device name
        case.write('Device: '+device+'\n')
        #Write the device model
        case.write('Model: '+model+'\n\n')
        # Write the issue
        case.write('Issue: '+issue)
        # Tell the user that an agent will get back to them and their case number
        sysp('An agent will get back to you. Your case number is: '+case_number)
        # Exit the program
        exit()
# Else (file was not found)
else:
    # Then device isn't supported, tell the user
    sysp('Sorry, we do not support this device!')
    # Exit the program
    exit()
