#include "lists.h"
#include <unistd.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: pointer, to an address, of to a singly linked list h
 * @number: number, to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp;
	int i = 0;

	if (*head == NULL || head == NULL)
		return (NULL);
	tmp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	while (tmp != NULL)
	{
		if (i == number - 1)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
		i++;
	}
	return (NULL);
}
