#include "lists.h"

/**
 * reverse_list - reverses singly linked list.
 * @head: pointer to the adress of head of list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev, *tmp, *next;

	prev = NULL;
	tmp = *head;
	next = NULL;
	while (tmp != NULL)
	{
		next = tmp->next;
		tmp->next = prev;
		prev = tmp;
		tmp = next;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the adress of head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *prev_slow, *fast, *half, *tmp, *tmp_half, *odd_half;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	slow = *head;
	fast = *head;
	half = NULL, odd_half = NULL, prev_slow = NULL;
	while (fast != NULL && fast->next != NULL && fast->next->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		odd_half = slow;
		slow = slow->next;
		if (odd_half->n != slow->n)
			return (0);
	}
	half = slow;
	reverse_list(&(half->next));
	tmp = *head;
	tmp_half = half->next;
	while (tmp_half != NULL)
	{
		if (tmp->n != tmp_half->n)
			return (0);
		tmp = tmp->next;
		tmp_half = tmp_half->next;
	}
	if (odd_half != NULL)
	{
		prev_slow->next = odd_half;
		odd_half->next = half;
	}
	return (1);
}
