#include <unistd.h>
#include "lists.h"

/**
 *check_cycle - checks if a singly linked list has a cycle in it.
 *
 * @head: pointer to a head node of the list
 *
 * Return: returns 0 if cycle is found, 1 if it doesn't
 */
int check_cycle(listint_t *head)
{
	listint_t *slow;
	listint_t *fast;

	if (head == NULL)
		return (0);
	slow = head;
	fast = head;
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (0);
	}
	return (1);
}
