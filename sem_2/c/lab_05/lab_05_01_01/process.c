#include <stdio.h>
#include <stdlib.h>

#include "process.h"

#define VALIDITY_ERROR -77

int process(FILE *f, int *first_max, int *second_max)
{
    int tmp;

    if (fscanf(f, "%d", first_max) != 1)
        return VALIDITY_ERROR;
    if (fscanf(f, "%d", second_max) != 1)
        return VALIDITY_ERROR;
    
    if (*second_max > *first_max)
    {
        tmp = *first_max;
        *first_max = *second_max;
        *second_max = tmp;    
    }

    while (fscanf(f, "%d", &tmp) == 1)
    {
        if (tmp > *first_max)
        {
            *second_max = *first_max;
            *first_max = tmp;
        }
        else if (tmp >= *second_max)
            *second_max = tmp;
    }

    return EXIT_SUCCESS;
}

