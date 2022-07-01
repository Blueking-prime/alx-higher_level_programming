#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if list is palindrome
 * @head: pointer to head of list
 * Return: 1 or 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i = 0, j;
	listint_t **list_list;

	current = *head;

	if (current == NULL || current->next == NULL)
		return (1);

	while (current->next != NULL)
	{
		current = current->next;
		i++;
	}
	current = *head;

	list_list = malloc(i * sizeof(listint_t));
	if (list_list == NULL)
		return (1);

	for (i = 0; current != NULL; i++)
	{
		list_list[i] = current;
		current = current->next;
	}

	j = i;
	for (i = 0; i != j; i++, j--)
	{
		if (list_list[i]->n != list_list[j - 1]->n)
			return (0);
	}

	return (1);
}
