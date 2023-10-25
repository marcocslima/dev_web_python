import sys

def verify_entry(entry):
    if len(sys.argv) != 2:
        return 1
    return 0

def transform_entry(entry):
    return entry.title()

def all_in(entry):

    entry = entry.split(",")
    for e in entry:
        if e.strip() == '':
            entry.remove(e)

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    caps = {value: key for key, value in capital_cities.items()}
    stas = {value: key for key, value in states.items()}

    for i in entry:
        location = transform_entry(i.strip())
        if location in caps:
            print(location, "is the capital of", stas[caps[location]])
        elif location in states:
            print(capital_cities[states[location]], "is the capital of",  location)
        else:
            print(i.strip(), "is neither a capital city nor a state")
    
if __name__ == '__main__':
    if verify_entry(sys.argv):
        exit
    else:
        all_in(sys.argv[1])