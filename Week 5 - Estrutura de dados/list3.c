#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
} node;

int main(void)
{
    node *list = NULL;

    for (int i = 0; i < 3; i++)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            // TODO: liberacao de todas as memorias quando malloc estiver pronto
            return 1;
        }
        n->number = get_int("number: ");
        n->next = NULL;

        // Se a lista for vazia, lista = n
        if (list == NULL)
        {
            list = n;
        }

        // Se o numero pertence ao comeco da lista
        else if (n->number < list->number)
        {
            n->next = list;
            list = n;
        }

        // Se o numero pertence ao final da lista e se a lista tiver enderecos prontos para
        // redirecionar
        else
        {
            //Interacao com todos os nodes (quadradinhos) que tem na lista
            for (node *ptr = list; ptr != NULL; ptr = ptr->next)
            {
                // Se esta no final da lista
                if (ptr->next == NULL)
                {
                    ptr->next = n;
                    break;
                }

                // Se esta no meio da lista
                else if (n->number < ptr->next->number)
                {
                    n->next = ptr->next;
                    ptr->next = n;
                    break;
                }
            }
        }
    }

    //print dos numeros
    for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    {
        printf("%i\n", ptr->number);
    }

    //time passes

    node *ptr=list;
    while(ptr!=NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }

    return 0;
}
