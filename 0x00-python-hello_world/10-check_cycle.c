#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 *
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 **/
int check_cycle(listint_t *list)
{
	listint_t *p = list;
	listint_t *q = list;

	if (list == NULL)
		return (0);
	while (p && q && q->next)
	{
		p = p->next;
		q = q->next->next;
		if (p == q)
			return (1);
	}
	return (0);
}
