'''

Facebook Email Bruter v1
Developers: Ñasir Ali (Tiger6117) &
            Azaz Tahir Selabi (azaztahir.azaztahir)

'''

class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f'''{Color.GREEN}
       __               _                 _    
      / _|             | |               | |   
     | |_ __ _  ___ ___| |__   ___   ___ | | __
     |  _/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
     | || (_| | (_|  __/ |_) | (_) | (_) |   < 
     |_| \__,_|\___\___|_.__/ \___/ \___/|_|\_\\
                Email Bruter By Tigerzplace.com
    {Color.ENDC}
''')


def validation(user_input, FOR):
    if FOR == 'email':
        if user_input.count("@") and user_input.count('.com') and user_input.count(" ") == 0:
            return 1
        else:
            return 0
    elif FOR == 'file':
        return user_input.count('.txt')


user_email = input("Enter email: ").lower()

if validation(user_email, 'email'):

    emails_list = input("Select emails list's : ")

    if validation(emails_list, 'file'):
        file = open(emails_list, "r")
        emails = list(set(file.read().split('\n')))
        # unique_emails = list(set(emails))
        file.close()
        check = 0

        for i in range(len(emails)):

            if len(user_email) == len(emails[i]):
                x = user_email.find("@")
                email = emails[i].lower()

                if user_email[0] == email[0] and email[x - 1] == user_email[x - 1]:
                    f = open("Found.txt", "a")
                    f.write(email + '\n')
                    check = 1

        if check:
            f.close()
            data = open("Found.txt", "r")
            emails = data.read().split('\n')
            print("Total email(s) found : " + str(len(emails) - 1))
            print("You can check email in Found.txt")
            data.close()
            check = 0
        else:
            print(f"{Color.FAIL}Email not found in the email(s) file :(")
            input(".")
    else:
        print(f"{Color.WARNING}Invalid emails file (use .txt file only)")
else:
    print(f"{Color.WARNING}Invalid email!!!")
    exit(1)
