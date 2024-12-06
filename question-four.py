# Program to create two sets of integers and find common elements
def common_elements():
    set1 = set(map(int, input("Enter integers for the first set separated by spaces: ").split()))
    set2 = set(map(int, input("Enter integers for the second set separated by spaces: ").split()))
    common_set = set1.intersection(set2)
    print(f"The common elements are: {common_set}")

common_elements()