import antigravity

def geohashing(latitude, longitude, datedow):
    return antigravity.geohash(latitude, longitude, datedow)

def main():
    geohashing(37.421542, -122.085589, b'2005-05-26-10458.68')

if __name__ == '__main__':
    main()