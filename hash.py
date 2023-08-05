# Cypher and Descypher Password with SHA-3-256

import hashlib
import getpass
import os

usage="""
    Usage: \n
        1 - Cypher to get HASH \n
        2 - Verify the password \n 
        3 - Exit \n
        4 - Usage \n
    """

def encrypt():
    pass_ = getpass.getpass("Write the password: ")
    h = hashlib.new('sha3_256')
    h.update(pass_.encode()) 
    hashed_password = h.hexdigest()
    print("Hash :", hashed_password)

def verify():
    stored_hash = input("Write the Hash: ")
    pass_ = getpass.getpass("Write the password to verify: ")
    
    h = hashlib.new('sha3_256')
    h.update(pass_.encode())
    hashed_password = h.hexdigest()
    
    if hashed_password == stored_hash:
        print("The password is correct!")
    else:
        print("The password is incorrect!")
    

def main():
    print(usage)
    while 1:
        print("____________________________________________\n")
        option=input("Select the option what do you want : ")
        match option:
            case "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                encrypt()
            case "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                verify()
            case "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            case "4":
                print(usage)
            case _:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Incorrect option!")

if __name__ == "__main__":
    main()
    pass
