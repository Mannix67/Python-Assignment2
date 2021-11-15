# This program calculates the change in length δ
import random
import re


# main function
def main():
    # All values input by the user should be real numbers (i.e. floating point values). This is checked by the function check(floatnum)
    print("This program calculates the change in length δ of a metal rod when an axial force is applied")

    P = input('Enter the Force P (in N:)')
    L = input('Enter the Length L (in m):')
    A = input('Enter the Area A (in m2):')
    E = input('Enter Youngs Modulus E (in Nm-2):')

    # The main function calls calc_delta() to calculate and return the change of length 𝛿 of a metal rod when a force is applied to it, according to the formula ab
    # δ = (float(P)*float(L))/(float(A)*float(E))
    # Here the main() function invokes calc_delta() with the values P,L,A and E input by the user as arguments

    δ = calc_delta(P, L, A, E)

    # and prints the calculated change in length δ (in meters,m)returned by the calc_delta(P,L,A,E)
    if δ is not None:
        print("The calculated change in length δ (in meters,m) is:", δ)


# Make a regular expression for
# identifying Floating point number
regex = '[+-]?[0-9]+\.[0-9]+'


# Define a function to
# check Floating point number
def check(floatnum):
    # pass the regular expression
    # and the string in search() method
    if (re.search(regex, floatnum)):
        return True

    else:
        return False


def calc_delta(P, L, A, E):
    if check(P) and check(L) and check(A) and check(E):  # Checks whether ALL the values entered are floating numbers
        print("All floating point!")
        # If ALL input of float type then
        # Calculate the change in length δ (in metres, 𝑚)

        δ = (float(P) * float(L)) / (float(A) * float(E))
        # and  print the Result
        return δ  # returns the calculated value to the Main()
    else:
        print("There is a problem with one of your inputs, ALL inputs should be float")


# call using  __name__ == "__main__":
if __name__ == "__main__":
    # call main ffunction
    main()

