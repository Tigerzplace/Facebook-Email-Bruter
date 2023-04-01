'''

Facebook Email Bruter v3
Developers: Ñasir Ali (Tiger6117) &
            Azaz Tahir Selabi (azaztahir.azaztahir)

'''
import os


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


print('''
       __               _                 _    
      / _|             | |               | |   
     | |_ __ _  ___ ___| |__   ___   ___ | | __
     |  _/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
     | || (_| | (_|  __/ |_) | (_) | (_) |   < 
     |_| \__,_|\___\___|_.__/ \___/ \___/|_|\_\\
                Email Bruter By Tigerzplace.com

''')


def close_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def validation(user_input, FOR):
    if FOR == 'email':
        if user_input.count("@") and user_input.count('.') and user_input.count(" ") == 0:
            return 1
        else:
            return 0
    elif FOR == 'file':
        return user_input.count('.txt')


try:
    user_email = input("Enter email: ").lower()

    if validation(user_email, 'email'):

        emails_list = input("Provide emails' list: ")

        if validation(emails_list, 'file'):
            file = open(emails_list, "r")
            emails = list(set(file.read().split('\n')))
            # unique_emails = list(set(emails))
            file.close()
            check = 0
            # for i in range(len(emails)):

            close_file('Found.txt')
            f = open("Found.txt", "a")

            for email in emails:
                email = email.lower().replace(" ", "")

                if len(user_email) == len(email):

                    # x = user_email.find("@")
                    # email = emails[i].lower()
                    email_ = email.split("@")
                    user_email_ = user_email.split("@")

                    if user_email_[1] == email_[1]:

                        if user_email_[0][0] == email_[0][0] and user_email_[0][-1] == email_[0][-1]:
                            # f = open("Found.txt", "a"
                            # feed = user_email, ' --> ', email, '\n'
                            # feed = f'{user_email} --> {email}\n'
                            feed = "{} --> {}\n".format(user_email, email)
                            # print(feed)
                            f.write(feed)
                            check = 1
            if check:
                f.close()
                data = open("Found.txt", "r")
                emails = data.read().split('\n')
                print("Total email(s) found : " + str(len(emails) - 1))
                print("You can check email(s) in Found.txt")
                data.close()
                check = 0
            else:
                f.close()
                close_file('Found.txt')
                print("Email not found in the email(s) list :(")
                input(".")
				
        else:
            print("Invalid emails file (use .txt file only)")
    else:
        print("Invalid email!!!")
        exit(1)

except Exception as e:
    print('Error:', e)
