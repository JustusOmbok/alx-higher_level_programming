#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - linked list is reversed
 * @head: head of the list pointer
 * Return: new head of the reversed linked list pointer
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks is linked list a palindrome
 * @head: head of list pointer
 * Return: 1 is palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *mid = NULL;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	second_half = reverse_list(slow);
	prev_slow->next = NULL;

	listint_t *p1 = *head;
	listint_t *p2 = second_half;

	while (p1 != NULL && p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			is_palindrome = 0;
			break;
		}
		p1 = p1->next;
		p2 = p2->next;
	}

	prev_slow->next = reverse_list(second_half);

	if (mid != NULL)
	{
		prev_slow->next = mid;
		mid->next = reverse_list(mid->next);
	}
	else
	{
		prev_slow->next = reverse_list(second_half);
	}

	return (is_palindrome);
}
