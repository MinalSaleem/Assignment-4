# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

# Accessing Elements:
# Write a function that:
# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.

# Modifying Elements:
# Write a function that:
# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.

# Slicing the List:
# Write a function that:
# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.

# Game Interaction:
# Create a simple text-based game that:
# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.



my_list = ["Apple", 13 , "Cerry", 5]

def access_element(list, index):
    try:
        return list[index]
    except IndexError:
        return "Index out of range!"

def modify_element(list, index, new_value):
    try:
        list[index] = new_value
        return list
    except IndexError:
        return "Index is out of range. Cannot modify!"

def slice_list(list, start, end):
    try:
        return list[start, end]
    except:
        return "Invalid slicing inputs!"

def main():

    while True:
        print("\n--- Index Game ---")
        print("Current List:", my_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")

        option = input("Enter your choice (1-4): ")

        if option == "1":
            index = int(input("Enter the index to access: "))
            result = access_element(my_list, index)
            print("Result:", result)

        elif option == "2":
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            if new_value.isdigit():
                new_value = int(new_value)
            result = modify_element(my_list, index, new_value)
            print("Updated List:", result)

        elif option == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced List:", result)

        elif option == "4":
            print("Thank you!")
            break

        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main()