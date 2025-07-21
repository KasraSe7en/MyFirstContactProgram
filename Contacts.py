my_contacts = {}
while True:
    user_input = int(input("""Please select your desired option:
1. Add contact  
2. Search contact  
3. Delete contact  
4. Show all contacts  
5. Exit  
"""))
    if user_input == 1:
        person_phone_name = input("Please enter the person's username: ")
        person_phone_num = input("Please enter the person's phone number: ")
        my_contacts[person_phone_name] = person_phone_num
        print("User added.")

    elif user_input == 2:
        username = input("Please enter the name of the desired person: ")
        if username in my_contacts:
            print(f"{username}'s phone number is {my_contacts[username]}")
        else:
            print("The person is not in the contacts.")

    elif user_input == 3:
        del_username = input("Please enter person's Username: ")
        if del_username not in my_contacts:
            print("User is not defined.")
        else:
            my_contacts.pop(del_username)
            print("User deleted.")

    elif user_input == 4:
        if not my_contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for name, number in my_contacts.items():
                print(f"{name}: {number}")

    elif user_input == 5:
        print("Exiting program...")
        break

    else:
        print("Please enter a defined operation.")
