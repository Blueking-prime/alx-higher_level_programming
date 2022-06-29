#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current != NULL)
		{
			if (current->n <= new->n && current->next->n >= new->n)
			{
				new->next = current->next;
				current->next = new;
				break;
			}
			else if (current == *head && current->n >= new->n)
			{
				new->next = *head;
				*head = new;
				break;
			}
			else if (current->n <= new->n && current->next == NULL)
			{
				current->next = new;
				break;
			}

			current = current->next;
		}
	}

	return (new);
}