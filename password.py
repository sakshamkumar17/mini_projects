import random
import string
Passdict = {}
try:
    with open("pwd.txt", "r") as file:
        for line in file:
            website , pwd = line.strip().split(":")
            Passdict[website] = pwd
except:
    pass

def generate_password():
    char = string.ascii_letters + string.digits + '!@#$%&'
    password = ''.join(random.choice(char) for _ in range(6))
    return password
while True:
    print("\n---Welcome to password manager---")
    print("1. Save Password")
    print("2. View Password")
    print("3. Create Password")
    print("4. Delete Password")
    print("5. Update Password")
    print("6. Exit..")

    choice = input("Enter your choice: ")
    if choice == "1":
        website = input("Enter website: ")
        pwd = input("Enter password: ")
        Passdict[website] = pwd
        
        with open("pwd.txt", "a") as file:
            file.write(f"{website}:{pwd}\n")
        print("Saved!!")

    elif choice == "2":
        if not Passdict:
            print("No data found")
        else:
            print("Here: ")
            for website, pwd in Passdict.items():
                print(f"{website} : {pwd}")
    
    elif choice == "3":
        website = input("Enter your site: ")
        pwd = generate_password()
        print(f"Your password is {pwd}")
        Passdict[website] = pwd
        
        with open("pwd.txt", "a") as file:
            file.write(f"{website}:{pwd}\n")
        print("Created & Saved!!")

    elif choice == "4":
        website = input("Enter site you want to delete: ")
        if website in Passdict:
          a = website + ':' + Passdict[website]
        
          with open("pwd.txt", "r") as file:
            content = file.read()
          content = content.replace(a + "\n", "")
          with open("pwd.txt" , "w") as file:
              file.write(content)
          del Passdict[website]
          print("Successfully Deleted!!")
        else:
          print("Site not found")
    
    elif choice == "5":
        website = input("Enter site whose password you want to update: ")
        if website in Passdict:
            prev_pass = Passdict[website]
            print(f"your previous password was: {prev_pass}")
            print("1. Change Manually")
            print("2. Change automatically")
            ch = input("choose: ")
            if ch == "1":
                pwd = input("Enter password: ")
                
            elif ch == "2":
                pwd = generate_password()
                print("New password", pwd)
            else:
                print("Sorry! Invalid choice")
                continue
            Passdict[website] = pwd
            with open("pwd.txt", "r") as file:
                content1 = file.read()
            
            old_line = f"{website}:{prev_pass}"
            new_line = f"{website}:{pwd}"

            content1 = content1.replace(old_line, new_line)
            with open("pwd.txt", "w") as file:
                file.write(content1)
            print("changed successfully!!")
        else:
            print("Data not found!!")

    elif choice == "6":
        print("Program Terminating...")
        break

    else:
        print("Invalid Value!!")


