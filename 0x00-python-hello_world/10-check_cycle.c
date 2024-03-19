#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle in it.
 * @list: pointer to the head of the list
 * Return: 0, if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *current = NULL;

    if (list == NULL)
        return (0);
    
    current = list;

    while (1)
    {
        current = current->next;

        if (current == NULL)
            return (0);
        if (current == list)
            break;
    }
    return (1);
}
