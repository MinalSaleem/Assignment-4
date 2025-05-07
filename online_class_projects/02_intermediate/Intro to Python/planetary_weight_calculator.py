# Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print the equivalent weight on that planet rounded to 2 decimal places if necessary.
# You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something other than one of the above planets.


GRAVITY_CONSTANTS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    planet_name = input("Enter a planet (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ")

    if planet_name in GRAVITY_CONSTANTS:
        planetary_weight = earth_weight * GRAVITY_CONSTANTS[planet_name]
        rounded_weight = round(planetary_weight, 2)
        print(f"The equivalent weight on {planet_name}: {rounded_weight}")
    else:
        print("Invalid Planet name. Please enter a valid Planet.")

if __name__ == "__main__":
    main()