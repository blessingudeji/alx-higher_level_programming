#include <Python.h>
/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: pointer.
 * Return:void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, a;
	PyObject *item;

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (a = 0; a < size; a++)
	{
		item = PyList_GetItem(p, a);
		printf("Element %ld: %s\n", a, Py_TYPE(item)->tp_name);
	}
}
