#q1 student number - 21129786

# to choose random element
import random


# main ffunction
def main():
    # print message to enter list of item and get it from user
    print(
        "This program accepts a list of items input by the user through the console, and then pick one of those items at random and print out the randomly chosen item to the console.")
    li = input('Enter list of item separating by "/" : ')

    # create list of element by spliting that string
    li1 = [i for i in li.split('/')]

    # printing the list
    print(li1)

    # print randomly selected item from list
    print(random.choice(li1))


# call using  __name__ == "__main__":
if __name__ == "__main__":
    # call main ffunction
    main()
