# Create a list called fruit_list that contains the following fruits: 'apple', 'banana', 'orange', 'grape', 'pineapple'. fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']

def main():

    fruit_list = ["apple","banana","orange","grape","pineapple"]
    
    list_length = len(fruit_list)
    print("Length of List: ",list_length)

    print(fruit_list)

    # Add 'mango' at the end of the list. 
    fruit_list.append('mango')

    # Print the updated list.
    for fruit in fruit_list:
        print(fruit, end=" , ")

if __name__ == "__main__":
    main()