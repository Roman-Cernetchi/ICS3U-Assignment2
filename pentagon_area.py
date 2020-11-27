#!/usr/bin/env python3
# Created by: Roman Cernetchi
# Created on: November 2020
# This program calculates area of a pentagon


def main():
    # This function calculates the area of a pentagon

    # Input
    print("Finding the Surface area of a Pentagon.")
    base = int(input("Enter the base of the pentagon (cm): "))
    height = int(input("Enter the height of the pentagon (cm): "))

    # process
    area = (1/2)*base*height

    # Output
    print("")
    print("Area is {}cm^2 ".format(area))


if __name__ == "__main__":
    main()
