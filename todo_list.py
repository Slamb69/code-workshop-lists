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

def delete_first_list_item(my_list):
    """Delete the first item from the list"""
    if my_list==[]:
        print "Nothing to delete"
        return None
    else:
        del my_list[0]  
        return my_list

def insert_in_position(my_list):
    """Inserts an item in a particular position in the list"""
    #print "Please input the index within the list"
    item = raw_input("Which item would you like to insert? ")
    print "The length of your list is", len(my_list), "items"
    position=int(raw_input("At which position would you like to insert the item? "))
    if position > len(my_list)+1:
        print "Your list isn't that long. Try again! "
    else:
        return my_list.insert(position-1,item)

def edit_item(my_list):
    """Edits an item by reassigning the index position"""
    print "Here's your list: ", view_list(my_list)
    edit_item = raw_input("Which item do you want to edit? ")
    replacement_item = raw_input("What is the replacement item? ")
    



def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Delete the first list item
    D. Insert item into a specific position in the list
    E. Edit an existing item 
    Q. Quit the program
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
            delete_first_list_item(my_list)
        elif choice == "D":
            insert_in_position(my_list)
        elif choice == "E":
            edit_item(my_list)
        elif choice == "Q":
            break
        else:
            print 'Unknown option.'

#-------------------------------------------------

my_list = []
display_main_menu(my_list)
  
