# Program to create a list of integers and compute their sum
def sum_of_integers():
    integers = input("Enter a list of integers separated by spaces: ").split()
    integers = [int(i) for i in integers]
    total_sum = sum(integers)
    print(f"The sum of the integers is: {total_sum}")

sum_of_integers()