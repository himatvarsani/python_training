'''
This code will not work -- Refer to the resources file...

You need to install the cryptography module inorder for this import to work
to install package you need to install my typing:
pip install cryptography -- if failed the import will not work
'''

from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode
fer = Fernet(key)

#Function - execuable and reusable code
def view():
    '''
    # You can use file = open('password.txt', 'a') but then you need 
    # to remember to close the file by file.close()
    # 'with' command will automatically close the file.
    # a: append mode - add of an existing file and creates a new file if file doesnt exist
    # w: always write the file
    # r: always read the file
    '''
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            # rstrip will take out the \n - new line - remove it
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", 
                  fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    
    # You can use file = open('password.txt', 'a') but then you need 
    # to remember to close the file by file.close()
    # 'with' command will automatically close the file.
    # a: append mode - add of an existing file and creates a new file if file doesnt exist
    # w: always write the file
    # r: always read the file
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones? (Type add or view) or press q to quit: ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue