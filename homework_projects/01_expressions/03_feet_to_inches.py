# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def main():
    feet = float(input("Enter feet: "))

    inches_to_feet = feet * 12

    print(str(feet) + " feet = " + str(inches_to_feet) + " inches" )

if __name__ == '__main__':
    main()