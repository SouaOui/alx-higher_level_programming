#include "lists.h"
/**
 * check_cycle - function that check if a singly linked list has a cycle
 * @head: pointer to a list
 * Return: 1 if yess and 0 if NO
 */
#include "lists.h"
int check_cycle(listint_t *head)
{
	listint_t *Tortoise = head;
	listint_t *Hare = head->next;

	if (head == NULL)
		return (0);
	while (Tortoise != Hare)
	{
		if (!Hare || !Hare->next)
			return (0);
		Tortoise = Tortoise->next;
		Hare = Hare->next->next;
	}
	return (1);
}
