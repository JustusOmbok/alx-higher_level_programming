#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - new node is inserted
 * @head: points to begining of singly linked list
 * @number: n value
 * Return: new node addrress
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *hold = *head;
	unsigned int i = 0;

	if (!(hold) || (*hold).n > number)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);

		(*new).n = number;
		(*new).next = *head;

		*head = new;

		return (*head);
	}

	while (hold)
	{
		if (!((*hold).next) || (*hold).next->n > number)
		{
			new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);
			(*new).n = number;
			(*new).next = (*hold).next;
			(*hold).next = new;
			return (ne);
		}
		hold = (*hold).next
			i++;
	}

	return (NULL);
}
