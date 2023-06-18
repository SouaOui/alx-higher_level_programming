#include "lists.h"
/**
 * insert_node - function that insert a node without losing sorting list
 * @head: pointer to head of the list
 * @number: data of the node
 * Return: the node to be added if Success or NULL if Failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_insert, *current, *previous;

	node_insert = malloc(sizeof(listint_t));
	if (node_insert == NULL)
		return (NULL);
	node_insert->n = number;
	if (*head == NULL || number < (*head)->n)
	{
		node_insert->next = *head;
		*head = node_insert;
		return (*head);
	}
	current = *head;
	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}
	node_insert->next = current;
	previous->next = node_insert;
	return (node_insert);
}
