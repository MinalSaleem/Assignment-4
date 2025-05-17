def main():

    name = input("Enter a name: ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    food = input("Enter a food item: ")
    color = input("Enter color: ")
    

    story = f"""
    Last weekend, {name} decided to visit {place}, hoping for a peaceful escape.
    Instead, the sky turned {adjective}, and out popped a mischievous {animal}!
    Before {name} could react, it began to {verb} in circles.
    Thinking quickly, {name} grabbed a {food}-flavored {object} and waved it around.
    Startled, the {animal} sprinted off, leaving behind a trail of {color} footprints.
    And that’s how {name} ended up as the accidental hero of {place}!
    """

    print(story)

if __name__ == "__main__":
    main()