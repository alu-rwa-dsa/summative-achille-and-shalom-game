
#I will start by defining a class 'Contact' with different attributes
import numpy
import matplotlib.pyplot as plt


class Contact:
    def __init__(self, name, phone_number, email_adress, birthday, category):
        self.name = name
        self.phone_number = phone_number
        self.email_adress = email_adress
        self.birthday = birthday
        self.category = category


#Below is the list Of the user's initial contacts
list_of_contacts = []

#To demonstate the use of other functions to the user I started by adding a number of contacts
contact1 = Contact("Mageza Shalom", "0787218771", "elsonmageza@gmail.com", "21/09/2000", "Family")
contact2 = Contact("Kidus Mengistu", "0781216728", "k.mengistu@alustudent.com", "14/04/2000", "Friend")

list_of_contacts.append(contact1)
list_of_contacts.append(contact2)


#here is where I defned my functions, to view, add, and remove a contact from the lsit of contacts

# The function for veiwing one contact's details
def view_contact(list_of_contact):
    print('The Existing Contact Names are:\n')
    for contact in list_of_contact:
        print("contact name:  ", contact.name)

    name = input('What is the name of contact you want to veiw?\n -->  ')
    for contact in list_of_contact:
        if name == contact.name:
            print("\n",contact.name, "contact details are: \nPhone Number: ",contact.phone_number,"\nEmail Adress: ",contact.email_adress,"\nBirthday: ",contact.birthday,"\nCategory: ",contact.category)
        
        else:
            print("\nContact Name Not Found!")

def adding_a_contact(list_of_contact):
    name = input("Please add the NAME of the person :\n -->  ")
    number = input("Please add the person's PHONE NUMBER :\n -->  ")
    email = input("Please add the person's EMAIL ADRESS :\n -->  ")
    birthday = input("When's the person's BIRTHDAY(DD/MM/YY):\n -->  ")
    category = input("Contact's category(Family/Friends/Work/Others):\n -->  ")

    contact = Contact(name, number, email, birthday, category)
    list_of_contact.append(contact)
    print("You have successfully added ", contact.name, " contact to your phonebook!")
 

def removing_contact(list_of_contact):
    print('The Existing Contact Names are:\n')
    for contact in list_of_contact:
        print("contact name:  ", contact.name)

    name = input('\nIn the above, what is the name the contact that you want to veiw?\n -->  ')
    for contact in list_of_contact:
        if name == contact.name:
            list_of_contact.remove(contact)
            print("You have sucessfully deleted the contact!")


def print_contact(list_of_contact):
    print("\nBelow is your current contact list:\n")
    #for veiwing this data in a table format
    print("____________________________________________________________________________________________")
    print("| Name Of The Contact         | Number Of The Contact        | Email Adress of Contact     |")
    print("+-----------------------------+------------------------------+-----------------------------+")
    for contact in list_of_contact:
        print("  {1}               | {2}                   | {3}                   ".format(3, contact.name, contact.phone_number, contact.email_adress))
        print("____________________________________________________________________________________________")


def delete_all(list_of_contact):
    alert = input("Are You sure you want to clear your contact list? (Y/N)").upper()
    if alert == "Y":
        list_of_contact.clear()
        print("You have deleted all contacts")
        
    else:
        print("Okay! Program Starting again")
            


#start the program
User_Name = input("\nHello & Welcome!\nPlease add your first name here:  ")
#Then I'll define the function that allows the OMONNDI to select the operation

def main():
    global User_Name
    print("\n",User_Name, " What operation are you trying to carry out\n\nLIST OF OPERATIONS:\n")
    print("1. View your contact list\n2. Add a contact to the list \n3. Remove(delete) a contact from the list \n4. View One contact's details \n5. Clear contact list\n\n")

    operation = int(input("insert '1', '2', '3', '4', or '5' \n-->  "))

    if operation == 1 :
        print_contact(list_of_contacts)
        other()

    elif operation == 2 :
        adding_a_contact(list_of_contacts)
        other()

    elif operation == 3 :
        removing_contact(list_of_contacts)
        other()

    elif operation == 4 :
        view_contact(list_of_contacts)
        other()

    elif operation == 5 :
        delete_all(list_of_contacts)
        other()

    else: 
        print("Wrong Selection! \nTry to insert '1', '2', '3', '4', or '5'")
        main()


def other():
    close = input("\nWould you like to continue or exit?\n'Y' for Continue and 'N' for exit \n-->   ").upper()

    if close == "Y":
        main()
    elif close == "N":
        exit("\nGOOD DAY!!!")
    else:
        print("Wrong Selection!! Try inserting 'Y' or 'N'")
        other()


main()
other()
