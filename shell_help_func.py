import os
import pathlib

def is_command_file(file_name):
    """going thrue the library and file if file_name is actually a file' id so it runs it"""
    
    flag = False
    for root, dirs, files in os.walk(pathlib.Path(__file__).parent.resolve(), topdown=False):
        for name in files:            
            if name == file_name:
                flag = True
                file_path = os.path.join(root, name)# gets the full file path
                print(file_path)
                exec(open(file_path).read())# execute the file
    return flag


def get_curr_dir():
    "change the global variable to the currents dir and return the current directory as a string"
    global curr_dir
    curr_dir = os.getcwd()# get the current directory
    # print("the current directory is" + curr_dir)
    return curr_dir
 

def print_dir(dire):
    """prints a list of all the files and libraries in the current directory"""
    my_dir= os.listdir(dire)
    dir_str = ""
    for det in my_dir:
        dir_str += det + "\n"
        print(det)
    return dir_str
def change_dir(direc):
    # change directory
    try:
        os.chdir(direc)
        print("Directory changed to: " + get_curr_dir())
    except:
        print("CHANGING DID NOT WORK")


def make_dir(dir_name, dir_path):
    """create a new directory with the path and name recieved from the client"""
    path = os.path.join(dir_path, dir_name)
    print(path)
    try: 
        os.mkdir(path)# creating the actuall directory
        print("Directory %s created" %dir_name)
    except:
        print("FAILED CREATING DIRECTORY")


def echo(str_list):
    "echos"
    my_str = ""
    for word in str_list:
        my_str += word + " "
    print(my_str)


def hello_py():
    try:
        exec(open("hello.py").read())
    except:
        print("THERE WAS AN ERROR RUNNING THE FILE")

def HexDump(path):  
    decimal_representation = int(open(path, 'rb').read(), 2)
    hexadecimal_string = hex(decimal_representation)
    print(hexadecimal_string)


def redirect(cmd):
    """redirects the str into a new file

    Args:
        cmd (str): the command
    """
    files = cmd.split(">")
    files[1] = files[1].replace(" ", "")
    if files[0][-1] == " ":
        files[0] = files[0][:len(files[0])-1]
    cmd, command_split = split_cmd(files[0])
    new_file_text = func_switcher(cmd, command_split)
    if new_file_text == -1:
        new_file_text = files[0]
    try:
        new_file = open(files[1], 'w')
        new_file.write(new_file_text)
        new_file.close()
    except:
        print("Error: the file was not found :(")

def is_our_func(func):
    """check if the the func exists

    Args:
        func (str): [description]
    """
    our_func_lst = ["dir"]
    if func in our_func_lst:
        return True
    return False

def find(word, txt="", path=""):
    """takes a txt file in str and if the word is found it prints the line with the word

    Args:
        word (str): the requested word
        txt (str): the txt we need to find it in
        path (str): the path the file we want to serch is in
    """
    # in case path was recieved
    lines_found = ""
    if txt == "":
        wanted_file = open(path, "r")
        for line in wanted_file:
            if word in line:
                print(line)
                lines_found += line + " "
    # in case string was recieved
    else:
        for line in txt:
            if word in line:
                print(line)
                lines_found += line + " "
    return lines_found

def func_switcher(cmd, cmd_det):
    
    # GOING THROUGH ALL THE CMD OPTIONS
    if cmd == "python":
        is_command_file(cmd_det[1])
    elif cmd == "dir":
        if len(cmd_det) == 1:
            get_curr_dir()
            return print_dir(curr_dir)
        else:# אם הלקוח ביקש ספרייה אחרת
            return print_dir(cmd_det[1])
    elif cmd == "cd":
        change_dir(cmd_det[1])
    elif cmd == "md":
        make_dir(cmd_det[1], cmd_det[2])        
    elif cmd == "echo":
        echo(cmd_det[1:])
    elif cmd == "hello.py":
        hello_py()
    elif cmd == "Hex_dump":
        HexDump(cmd_det[1])
    elif cmd == "find":
        if len(cmd_det) == 3:# if it is find with a path to a file
            return find(cmd_det[1].strip('"'), "", cmd_det[2])
        else:# if it is find called through piping
            return find(cmd_det[1].strip('"'), cmd_det[0], "")
    return -1
def split_cmd(command):
    """responsible for spliting the base cmd recieved from the client

    Args:
        command (str): the client's command

    Returns:
        cmd: the command name
        command_split: list of the command parts
    """
    command_split = command.split(" ")
    cmd = command_split[0]
    return cmd, command_split

def pipe(func1, func2):
    """take the output of the first command and givei t to the second command as an argument

    Args:
        func1 (str): the first command
        func2 (str): the second command
    """
    # handke the command spliting
    try:
        cmd, command_split = split_cmd(func1)# devides to cmd itself and a list includes all the part of the command icluding the cmd
        first_command_output = func_switcher(cmd, command_split)
    except:
        print("ERROR - FIRST COMMAND WENT WRONG")
    try:
        cmd, command_split = split_cmd(func2 + " " + first_command_output)# devides to cmd itself and a list includes all the part of the command icluding the cmd
        # command_split[0] = first_command_output# replaces in the list the func1 output eith the cmd
        func_switcher(cmd, command_split)
    except:
        print("EROOR - SECOND COMMAND WENT WRONG")


