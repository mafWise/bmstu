#include <stdio.h>
#include <stdlib.h>

#include "calc_funcs.h"

void get_max_and_min(FILE *f, double *max, double *min)
{
    int flag = 1;
    double tmp;

    while (fscanf(f, "%lf", &tmp) == 1)
    {
        if (tmp > *max || flag == 1)
            *max = tmp;
        if (tmp < *min || flag == 1)
            *min = tmp;
        flag = 0;
    }
}


void get_quantity(FILE *f, int *quantity, double max, double min)
{
    double tmp;
    double mean = (min + max) / 2;

    while (fscanf(f, "%lf", &tmp) == 1)
    {
        if (tmp > mean)
            (*quantity)++;
    }
}
