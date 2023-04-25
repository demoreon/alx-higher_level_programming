#!/usr/bin/python3
"""

This module features a function to prints identation

"""


def text_indentation(text):
    """ Function that prints indentation """

    delimiters = ".:?"
    if type(text) is not str:
        raise TypeError('text must be a string')

    newT = text
    for delim in delimiters:
        lines =  newT.split(delim)
        newT = ""
        for line in lines:
            line = line.strip(" ")
            if newT == "":
                newT = line + delim
            else:
                newT += "\n\n" + line + delim
    print(newT[:-3], end='')
