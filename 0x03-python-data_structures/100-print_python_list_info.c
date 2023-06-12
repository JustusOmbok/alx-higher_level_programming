#include <Python.h>
#include <stdio.h>

void print_python_list_info(Py0object *p)
{
	Py_ssize_t size, alloc, i;
	Py0bject *obj;

	size = PyList_Size(p);
	alloc = ((PyList0bject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", alloc);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
