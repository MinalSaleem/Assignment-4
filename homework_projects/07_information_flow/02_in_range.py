# Problem Statement
# Implement the following function which takes in 3 integers as parameters:
# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """


def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower number: "))
    high = int(input("Enter the upper number: "))  

    result = in_range(n,low,high)
    print("Is the number in range?", result)

def in_range(n, low, high): 
    """ 
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low. 
    """

    if n >= low and n <= high:
        return True
    return False

if __name__ == '__main__':
    main()   