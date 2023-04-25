#!/usr/bin/python3
""" An upgrade to my matrix mul function """


def matrix_mul(m_a, m_b):
    """ Function to perform valid multipliations """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for i in m_a:
        if len(i) == 0:
            raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for i in m_b:
        if len(i) == 0:
            raise ValueError("m_b can't be empty")
    for rows in m_a:
        for i in rows:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for rows in m_b:
        for i in rows:
            if not isinstance(i, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    for rows in m_a:
        if len(m_a[0]) != len(rows):
            raise TypeError("each row of m_a must be of the same size")
    for rows in m_b:
        if len(m_b[0]) != len(rows):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")
