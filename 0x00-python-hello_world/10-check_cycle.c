#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the list
 *
 * Return: integer
 */

int check_cycle(listint_t *list)
{
	listint_t *current = NULL;

	if (list == NULL)
		return (0);

	current = list;
	while (current != NULL)
	{	
		current  = current->next;
		if (current == NULL)
			return (0);
		if (current == list)
			break;
	}
	return (1);
}
