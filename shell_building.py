import os.path
from shell_help_func import *


def get_curr_dir():
    "change the global variable to the currents dir and return the current directory as a string"
    global curr_dir
    curr_dir = os.getcwd()# get the current directory
    print("the current directory is" + curr_dir)
    return curr_dir


curr_dir = ""# get the current directory
get_curr_dir()
file_path = ""
cmd = ""# gets first input from the uder to start the while
while cmd!= "exit":
    #  going through all the files looking if on's name identical to the command entered
    command = input("ENTER YOUR COMMAND: ")
    command_split = command.split(" ")
    cmd = command_split[0]
    print("the command you entered is: ", cmd)
    is_command_file(cmd)
    # GOING THROUGH ALL THE CMD OPTIONS
    if cmd == "dir":
        get_curr_dir()
        print_dir(curr_dir)
    elif cmd == "cd":
        change_dir(command_split[1])
        get_curr_dir()
    elif cmd == "md":
        make_dir(command_split[1], command_split[2])        
    elif cmd == "echo":
        echo(command_split[1:])
    elif cmd == "hello.py":
        hello_py()
    elif cmd == "Hex_dump":
        HexDmp(command_split[1])
    elif cmd == "pipe":
        pass
    elif cmd == "Redirection":
        pass
    elif cmd == "find":
        pass
    
    
