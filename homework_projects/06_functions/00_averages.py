# Write a function that takes two numbers and finds the average between the two.

def average(x: float, y: float):
    """
    Returns the number which is half way between a and b
    """
    sum = x + y
    return sum / 2

def main():
    a = float(input("Enter first number (a): "))
    b = float(input("Enter second number (b): "))
    c = float(input("Enter third number (c): "))
    d = float(input("Enter fourth number (d): "))

    avg_1 = average(a, b)
    avg_2 = average(c, d)
    
    final = average(avg_1, avg_2)
    print("First two number average (avg_1): ", avg_1)
    print("Second two numbers average (avg_2): ", avg_2)
    print("Final average: ", final)

if __name__ == '__main__':
    main()