'''
Write a Python Program using text files
to create and maintain a Phone Book.
The Phone Book will display the
following Menu and will support
the corresponding functionality

*** Phone Book Menu ***
Enter 1,2,3 or 4:
Enter 1 To Display Your Contacts Records
Enter 2 To Add a New Contact Record a new contact
Enter 3 To search your contacts
Enter 4 To Quit
**********************

author: Indraneel Mandal
'''

# Phone Book Program

import pandas as pd


Name=[]
Phone=[]
Email_Address=[]
 

def book1(): 
    df={"Name":Name,"Phone No.":Phone,"Email":Email_Address}
    b=pd.DataFrame(data=df)

    

def show_main_menu():
    ''' Show main menu for Phone Book Program '''
    print("\n   *** Phone Book Menu ***\n"+
          "author: INDRANEEL MANDAL (c)\n"+
          "------------------------------------------\n"+
          "Enter 1,2,3 or 4:\n"+
          "Enter 1 To Display Your Contacts Records\n" +
          "Enter 2 To Add a New Contact Record\n"+
          "Enter 3 To search your contacts\n"+
          "Enter 4 To delete a contact\n" +
          "Enter 5 To update\n" +
          "Enter 6 To Quit\n**********************")
    choice = input("Enter your choice: ")
    if choice == "1":
        display_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        update_contact()
    elif choice == "6":
        print("Good Bye")
    else:
        print("Invalid choice. Please choose a valid option.")

def display_contacts():
    ''' Display all contacts '''
    print("\n   *** Display Contacts ***\n")
    # for i in range(len(Name)):
    #     print(f"Name: {Name[i]}")
    #     print(f"Phone: {Phone[i]}")
    #     print(f"Email: {Email_Address[i]}")
    #     print("-------------------------------")
    #     print("\n")
    a=pd.read_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\inter\\PHONEBOOK.csv")
    print(a)
    show_main_menu()

def add_contact():
    ''' Add a new contact '''
    print("\n   *** Add Contact ***\n")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    Name.append(name)
    Phone.append(phone)
    Email_Address.append(email)
    print(f"Contact {name} added successfully")
    g=book1()
    new_df={"Name":Name,"Phone No.":Phone,"Email":Email_Address}
    oh=pd.DataFrame(new_df)
    g=pd.concat([g,oh],ignore_index=True)
    g.to_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\inter\\PHONEBOOK.csv",index=False,mode='a+')
    show_main_menu()

def search_contact():
    ''' Search a contact '''
    print("\n   *** Search Contact ***\n")
    df = pd.read_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\inter\\PHONEBOOK.csv")
    if df.empty:
        print("\nNo contacts found.")
    else:
        name = input("Enter Name to search: ").strip()
        results = df[df["Name"].str.lower() == name.lower()]
        
        if results.empty:
            print("\nContact not found.")
        else:
            print("\n*** Contact Found ***")
            print(results.to_string(index=False))
    # for i in range(len(Name)):
    #     if name == Name[i]:
    #         print(f"Name: {Name[i]}")
    #         print(f"Phone: {Phone[i]}")
    #         print(f"Email: {Email_Address[i]}")
    #         break
    #     else:
    #         print("Contact not found")
    #         show_main_menu()
    show_main_menu()        

def delete_contact():
    ''' Delete a contact '''
    print("\n   *** Delete Contact ***\n")
    # name = input("Enter Name: ")
    x=pd.read_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\inter\\PHONEBOOK.csv")
    nhk=pd.DataFrame(x)
    # if nhk.loc(axis=1)==name:
    #     nhk.pop(name)
    #     print(nhk)
    # else:
    #     print(f"The contact was not found")/

    name = input("Enter Name to delete: ").strip()
    new_df = nhk[nhk["Name"].str.lower() != name.lower()]

    if len(new_df) == len(nhk):
        print("\nContact not found.")
    else:
        new_df.to_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\inter\\PHONEBOOK.csv",index=False,mode='a+',header=False)
        print(f"Contact '{name}' deleted successfully.\n")

    show_main_menu()

def update_contact():
    ''' Update a contact '''
    print("\n   *** Update Contact ***\n")
    df = pd.read_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\inter\\PHONEBOOK.csv")
    name = input("Enter Name to update: ").strip()
    results = df[df["Name"].str.lower() == name.lower()]
    if results.empty:
        print("\nContact not found.")
    else:
        print("\n*** Contact Found ***")
        print(results.to_string(index=False))
        print("\n   *** Update Contact ***\n")
        phone = input("Enter new Phone: ").strip()
        email = input("Enter new Email: ").strip()
        results.loc[0, 'Phone'] = phone
        results.loc[0, 'Email'] = email
        results.to_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\inter\\PHONEBOOK.csv")
        print(f"Contact '{name}' updated successfully.\n")
    show_main_menu()

show_main_menu()
