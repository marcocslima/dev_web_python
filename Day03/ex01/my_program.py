import sys
from local_lib.path import Path

def my_program():

    path_dir = Path('./my_folder')
    
    if not path_dir.isdir():
        Path.mkdir('./my_folder')

    file_ = open(path_dir + '/my_file', 'w')
    file_.write("Hello")
    file_.close()

    with open(path_dir + '/my_file', "r") as arq:
        print(arq.read())
    arq.close()

if __name__ == '__main__':
    my_program()
    