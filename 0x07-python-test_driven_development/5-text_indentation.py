#!/usr/bin/python3
"""

This module features a function to prints identation

"""


def text_indentation(text):
    """ Function that prints indentation """


    delimiters = ".:?"
    if type(text) is not str:
        raise TypeError('text must be a string')

    #lines = new.replace(delim, delim + '*')
    new = text

    for delim in ".:?":
        lines = new.split(delim)
        new = ""

        for line in lines:
            line = line.strip(" ")

            if new is "":
                new = line + delim
            else:
                new += "\n\n" + line + delim

    print(new[:-3], end='')

    # Example usage
#text_indentation("Betty: Holberton? Python is. cool ")
