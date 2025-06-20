#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // time passes

    // realoca todo o conteudo da variavel list dentro da tmp, dessa forma ha necessidade de ter um
    // loop interno para copiar dado a dado, assim deixando o codigo mais limpo e dinamico
    
    int *tmp = realloc(list, 4 * sizeof(int));
    if (tmp == NULL)
    {
        return 1;
    }

    tmp[3] = 4;

    free(list);

    list = tmp;

    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    // time passes

    free(list);
    return 0;
}
