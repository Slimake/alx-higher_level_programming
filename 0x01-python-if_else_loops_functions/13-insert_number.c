#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer
 * Return: the address of the new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *prev_node = NULL;
    listint_t *next_node = NULL;
    listint_t *current = NULL;
    listint_t *new = NULL;

    /* Check if head is NULL, return NULL */
    if (*head == NULL)
        return NULL;
    
    /* Then we create a new node */
    new = malloc(sizeof(listint_t));

    if (new == NULL)
        return NULL;

    current = *head;

    /*
       Cycle through the node and compare the current->n 
       with number, if they match, store current in prev_node 
       and current->next in next_node
     */
    while (current != NULL)
    {
        if (current->next->n >= number)
        {
            prev_node = current;
            next_node = current->next;
            break;
        }
        current = current->next;
    }

    prev_node->next = new;

    new->n = number;
    new->next = next_node;

    return new;
}
