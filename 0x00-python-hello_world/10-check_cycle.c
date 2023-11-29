#include "lists.h"
/**
 * check_cycle - beginning of cycle checks
 * @list: lnked list of cycle 
 * Return: 1, 0 if list has cycle and not respectively
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list, *f = list;
	if (!list)
		return (0);
	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
