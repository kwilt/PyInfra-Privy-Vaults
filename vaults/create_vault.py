import privy
from getpass import getpass
from pathlib import Path

filename = input("Enter name of new password file: ")
password = getpass("Enter the decryption password: ")
data_input = getpass("Enter the password to be hidden: ")

data = bytes(data_input, encoding="utf-8")
filepath = Path(__file__).with_name(filename) # output file in same directory as the script

with open(filepath, "w+b") as encrypted_data:
    encrypted_data.write(privy.hide(data, password).encode())
