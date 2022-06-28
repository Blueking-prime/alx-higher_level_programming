#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if the list cycles
 * @h: pointer to head of list
 * Return: 1 or 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *hd = list;
    listint_t *curr;
	int i = 0, j;
	listint_t **list_of_nodes;

	curr = hd;
	while(curr->next != NULL)
	{
        curr = curr->next;
		i++;
	}

	list_of_nodes = malloc(i * sizeof(listint_t));
	if (list_of_nodes == NULL)
	{
		return (0);
	}

	curr = hd;
	i = 0;
	while(curr->next != NULL)
	{
        curr = curr->next;
		list_of_nodes[i] = curr;
	}

	for (i = 0; list_of_nodes[i] != NULL; i++)
	{
		for (j = 0; list_of_nodes[j] != NULL; j++)
		{
			if (i == j)
				continue;
			if (list_of_nodes[i] == list_of_nodes[j])
				return (1);
		}
	}
	free(list_of_nodes);

	return (0);
}