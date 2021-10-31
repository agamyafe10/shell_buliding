import os.path
from shell_help_func import *


curr_dir = ""# get the current directory
get_curr_dir()
file_path = ""
cmd = ""# gets first input from the uder to start the while
while cmd!= "exit":\
    #  going through all the files looking if on's name identical to the command entered
    cmd = input("ENTER YOUR COMMAND: ")
    print("the command you entered is: ", cmd)
    is_command_file(cmd)
    # GOING THROUGH ALL THE CMD OPTIONS
    if cmd == "dir":
        print_dir(curr_dir)
    elif cmd == "cd":
        change_dir()
    elif cmd == "md":
        make_dir()        
    elif cmd == "echo":
        pass
    elif cmd == "hello.py":
        pass
    elif cmd == "Hex_dump":
        pass
    elif cmd == "pipe":
        pass
    elif cmd == "Redirection":
        pass
    elif cmd == "find":
        pass
    
    
def get_curr_dir():
    "change the global variable to the currents dir and return the current directory as a string"
    global curr_dir
    curr_dir = os.getcwd()# get the current directory
    print("the current directory is" + curr_dir)
    return curr_dir
