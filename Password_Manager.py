import os
from cryptography.fernet import Fernet

#This Function should be run once for creating the encryption key , and then should be removed from the set of code
#def write_Key():
#   key = Fernet.generate_key()
#   with open("key.key",'wb')as key_file:
#       key_file.write(key)

#write_Key()

def Load_Key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = Load_Key()
fer = Fernet(key)

def View():
    with open("Password.txt",'r')as f:
        for line in f.readlines():
            data = line.rstrip()
            user , password = data.split("|")
            print("UserName : "+user + "Password : "+ fer.decrypt(password.encode()).decode())

def Add():
    Name = input("UserName: ")
    pwd = input("Password : ")

    with open("Password.txt",'a')as f:
        f.write(Name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input(f"To create New Password Type:Add \nTo View Existing Passwords Type:View \nTo Exit Type:Quit \n").upper()
    if mode == "QUIT":
        exit(0)
    if mode == "VIEW":
        View()
    elif mode == "ADD":
        Add()
    else:
        print("Invalid Mode Entry")
        continue
