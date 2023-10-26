# Function to search for a key element in a list of elements
def search_element():
    # Input the number of elements
    n = int(input("Enter the number of elements: "))
    # Input the elements and store them in a list
    elements = [int(input(f"Enter {i + 1}: ")) for i in range(n)]
    # Input the key element to search for
    key = int(input("Enter the key element: "))

    found = False
    for i in range(n):
        if elements[i] == key:
            found = True
            index = i + 1
            break

    if found:
        print(f"Key element {key} is found at index {index}")
    else:
        print(f"Key element {key} is not found")

# Call the search_element function to execute the search
search_element()
