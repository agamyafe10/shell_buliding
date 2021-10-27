import os.path
from shell_help_func import *


file_path = ""
client = ""# gets first input from the uder to start the while
while client != "exit":
    client = input("ENTER YOUR COMMAND")
    print("the command you entered is: ", client)
    is_command_file(client)# going through all the files looking if on's name identical to the command entered
