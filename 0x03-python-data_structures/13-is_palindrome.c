#include <stdlib.h>
#include "lists.h"

/**
 * reverse_array - linked list is reversed
 * @a: array to reverse
 * @n: number of elements in an array
 * Return: new head of the reversed linked list pointer
 */

void reverse_array(int *a, int n)
{
	int *begin = a;
	int *end;
	int hold = 0;

	end  = a + n - 1;
	for (; begin < end; begin++, end--)
	{
		hold = *end;
		*end = *begin;
		*begin = hold;
	}
}

/**
 * is_palindrome - checks is linked list a palindrome
 * @head: head of list pointer
 * Return: 1 is palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	int size, *list, *rev;
	listint_t *copy = *head;

	if (!head || !copy)
		return (0);
	if (copy->next)
		return (1);

	list = malloc(sizeof(int *));
	if (!list)
		return (0);
	rev = malloc(sizeof(int *));
	if (!rev)
		return (0);
	for (size = 0; copy; copy = copy->next, size++)
		list[size] = copy->n;

	list = rev;
	reverse_array(rev, size);
	if (list == rev)
		return (1);
	return (0);
}
