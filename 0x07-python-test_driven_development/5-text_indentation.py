#!/usr/bin/python3
"""

This module features a function to prints identation

"""


def text_indentation(text):
    """ Function that prints indentation """

    if type(text) is not str:
        raise TypeError('text must be a string')

    delimiters = [".", ":", "?"]
    # Replace each delimiter with a single common delimiter character
    for delimiter in delimiters:
        text = text.replace(delimiter, delimiter + "\n")

    lines = text.split('\n')
    for line in lines:
        if line == lines[-1]:
            line = line.lstrip().rstrip()
            for ln in line:
                if ln not in delimiters:
                    print(ln, end='')
                else:
                    print(ln, end="\n\n")
        else:
            print(line.lstrip().rstrip(), end="\n\n")
