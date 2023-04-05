#include "lists.h"

/**
 * check_cycle - scans a linked list contains a cycle i.e repeats
 *
 * @list: linked list to check
 *
 * Return: 0 or 1
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
