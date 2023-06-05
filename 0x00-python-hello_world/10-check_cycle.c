#include "lists.h"
/**
 * check_cycle - loop is found in linked list
 * @list: lists starting point
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && (*fast).next)
	{
		slow = (*slow).next;
		fast = (*(*fast).next).next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
