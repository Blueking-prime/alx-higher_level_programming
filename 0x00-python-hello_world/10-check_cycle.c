#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if the list cycles
 * @list: pointer to head of list
 * Return: 1 or 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *curr;

	if (list == NULL)
	{
		return (0);
	}
	curr = list;
	while (curr->next != NULL)
	{
		if (curr->next == list)
		{
			return (1);
		}
		curr = curr->next;
	}

	return (0);
}
