import os

def is_command_file(file_name):
    """going thrue the library and file if file_name is actually a file' id so it runs it"""
    "
        for root, dirs, files in os.walk('C:/Users/cyber/Desktop/agam', topdown=False):
            for name in files:            
                if name == file_name:
                    file_path = os.path.join(root, name)# gets the full file path
                    print(file_path)
                    exec(open(file_path).read())# execute the file