#include <stdio.h>
#include "Python.h"

/**
 * print_python_string - A function that print any string including unicodes
 *
 * @p: The PyObject
 */

void print_python_string(PyObject *p)
{
	PyObject *encoded_str;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	encoded_str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %s\n", PyBytes_AsString(encoded_str));
}
