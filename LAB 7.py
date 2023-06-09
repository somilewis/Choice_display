# Lewis Muthomi
# 1250 01
# october/5/2022
# Lab 7

# This program will dispaly a sentence based on the choice of your letter

# User greeting
print('Welcome to the display sentence program')


# Get user input
choice = input('Please enter an A, B or C to display a particular sentence.Use capital letter: ')
print()


# Display action taken
if choice == 'A':
    print('You got an Apple!!!')
elif choice == 'B':
    print('You got a Banana!')
elif choice == 'C':
    print('You got a Coconut!')
else:
    print('Invalid entry!!!')

    
# Exit message
print()
print('Have a nice day!!!')
