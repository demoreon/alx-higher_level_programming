#!/usr/bin/python3
""" Python script to multiply two or more matrices """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    return (np.matmul(m_a, m_b))
