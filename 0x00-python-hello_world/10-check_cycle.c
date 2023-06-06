#include "lists.h"

/**
 * check_cycle - checks runtime cycle of linked list
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list;
	listint_t *ptr2 = list;

	if (list == false)
		return (0);

	while (ptr1 && ptr2 && ptr2->next)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
			return (1);
	}

	return (0);
}
