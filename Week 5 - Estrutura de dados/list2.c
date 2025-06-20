#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

// este programa realiza um processo de pedir 3 numeros ao usuario 1 por vez e no fim printar eles
// do ultimo para o primeiro, para isto esta sendo utilizado a estruturacao de node, para fazer a
// alocacao dinamica na memoria
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
            //TODO: liberacao de todas as memorias quando malloc estiver pronto
            return 1;
        }
        n->number = get_int("number: ");
        n->next = NULL;

        // Se a lista for vazia, lista = n
        if (list == NULL)
        {
            list = n;
        }

        // se a lista tiver enderecos prontos para redirecionar
        else
        {
            for (node *ptr = list; ptr != NULL; ptr = ptr->next)
            {
                if (ptr->next == NULL)
                {
                    ptr->next = n;
                    break;
                }
            }
        }
    }

    // time passes

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
