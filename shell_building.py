import os.path
from shell_help_func import *



    
""" main code """
curr_dir = ""# get the current directory
get_curr_dir()
file_path = ""
cmd = ""# gets first input from the uder to start the while
while cmd!= "exit":
    #  going through all the files looking if on's name identical to the command entered
    command = input("ENTER YOUR COMMAND: ")
    if '|' in command:
        # devides the input to the basic function
        command_split = command.split("|")
        first_command = command_split[0].strip(" ")
        second_command = command_split[1].strip(" ")
        pipe(first_command, second_command)
    if '>' in command:
        redirect(command)
    else:   
        cmd, command_split = split_cmd(command)
        print("the command you entered is: ", cmd)
        func_switcher(cmd, command_split)

5
