"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""
    item= raw_input("What item to add? ")
    #my_list.append(item)
    #print my_list 
    return my_list.append(item)
     
    #print "The add_to_list function has not yet been written"


def view_list(my_list):
    """Print each item in the list."""
    
    for each in my_list:
        print each
    #print "The view_list function has not yet been written"


def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Quit the program
    >>> """
    
    while True:
        # Collect input and include your if/elif/else statements here.
        
        print user_options
        choice = raw_input("Choose an option from the menu. ")
        if choice == 'A':
            add_to_list(my_list)
        elif choice == "B":
            view_list(my_list)
        elif choice == "C":
            break
        else:
            print 'Unknown option.'

#-------------------------------------------------

my_list = []
display_main_menu(my_list)
  
