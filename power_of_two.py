#!/usr/bin/env python3
# Created By: Maeva Tchuenga
# Date: 09, 12 2026
# this program is to find if a number is a power of two.


def main():
    user_number = input("enter a whole number: ")

    try:
        if user_number == int("whole_number_str"):
            if user_number < 0:
                print("the user_number is a negative number")

                for user_number in range(0, 10):
                    counter = 0
                    counter <= user_number
                    counter += 1
                    counter **= 2
                    print(f"the {user_number}**2 has a {counter}**2 ")
                return
            else:
                print(f"the {counter}**2 is greater than the {user_number}**2")

    except:
        ValueError
    print("sorry! user_input is not an integer")


if __name__ == " __main__":
    main()
