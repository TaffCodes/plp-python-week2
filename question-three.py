# Program to store information about a person in a dictionary
def person_info():
    person = {}
    person['name'] = input("Enter your name: ")
    person['age'] = input("Enter your age: ")
    person['favorite_color'] = input("Enter your favorite color: ")
    print(person)

person_info()