import sys

def state(capital_city):
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
    if capital_city in caps:
        print(stas[caps[capital_city]])
        return
    print("Unknown capital city")
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit
    else:
        state(sys.argv[1]) 