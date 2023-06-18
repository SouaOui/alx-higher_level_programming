#include "lists.h"
/**
 * check_cycle - function that check if a singly linked list has a cycle
 * @head: pointer to a list
 * Return: 1 if yess and 0 if NO
 */
int check_cycle(listint_t *head)
{
	listint_t *Tortoise;
	listint_t *Hare;

	if (head == NULL)
		return (0);
	Tortoise = head;
	Hare = head->next;
	while (Tortoise != Hare)
	{
		Tortoise = Tortoise->next;
		Hare = Hare->next->next;
	}
	return (1);
}

