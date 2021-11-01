import os

def is_command_file(file_name):
    """going thrue the library and file if file_name is actually a file' id so it runs it"""
    
    flag = False
    for root, dirs, files in os.walk('C:/Users/cyber/Desktop/agam', topdown=False):
        for name in files:            
            if name == file_name:
                flag = True
                file_path = os.path.join(root, name)# gets the full file path
                print(file_path)
                exec(open(file_path).read())# execute the file
    return flag


def print_dir(dire):
    """prints a list of all the files and libraries in the current directory"""
    my_dir= os.listdir(dire)
    for det in my_dir:
        print(det)
    

def change_dir(direc):
    # change directory
    try:
        os.chdir(direc)
        print("directory changed to" + direc)
    except:
        print("CHANGING DID NOT WORK")


def make_dir(dir_name, dir_path):
    """create a new directory with the path and name recieved from the client"""
    path = os.path.join(dir_path, dir_name)
    print(path)
    try: 
        os.mkdir(path)# creating the actuall directory
        print("Directory '%s' created", dir_name)
    except:
        print("FAILED CREATING DIRECTORY")


def echo(str_list):
    "echos"
    my_str = ""
    for word in str_list:
        my_str += word + " "
    print(my_str.upper())


def hello_py():
    try:
        exec(open("hello.py").read())
    except:
        print("THERE WAS AN ERROR RUNNING THE FILE")

def HexDump(path):  
    decimal_representation = int(open(path).read(), 2)
    hexadecimal_string = hex(decimal_representation)
    print(hexadecimal_string)
