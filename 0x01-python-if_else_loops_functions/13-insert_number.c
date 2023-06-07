#include "lists.h"
/**
 * insert_node - inserts number into a sorted singly linked list
 * @head: head of list
 * @number: number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current,*new;

	current = *head;
	new = malloc(sizeof(listint_t));
	if(new == false)
		return(NULL);
	new->n = number;
	new->next = NULL;
	if((*head) == NULL)
	{
		*head = new;
		return(new);
	}
	else if((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return(new);
	}
	else
	{
		while(current->next != NULL)
		{
			if(current->next->n >= number)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			current = current->next;
		}
		new->next = NULL;
		current->next = new;
		return(new);
	}
	return(NULL);
}
