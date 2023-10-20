import settings
import sys
import os

def verify_entry(entry):
    if len(sys.argv) != 2:
        print('wrong number of arguments!')
        return 1
    if (sys.argv[1].split('.')[1] != 'template'):
        print('wrong file extension!')
        return 1
    if not os.path.exists(sys.argv[1]):
        print('non-existing file!')
        return 1
    return 0

def render(entry):
    myCV = open(entry, "r")
    cv = open("cv.html", "w")
    for l in myCV:
        if '{name}' in l:
            l = l.replace('{name}', settings.name)
        elif '{surname}' in l:
            l = l.replace('{surname}', settings.surname)
        elif '{age}' in l:
            l = l.replace('{age}', str(settings.age))
        elif '{profession}' in l:
            l = l.replace('{profession}', settings.profession)
        cv.write(l)

    myCV.close()
    cv.close()

if __name__ == '__main__':
    if verify_entry(sys.argv):
        exit
    else:
        render(sys.argv[1])