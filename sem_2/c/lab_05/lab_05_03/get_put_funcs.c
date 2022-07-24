#include <stdio.h>
#include <stdlib.h>

#include "file_funcs.h"

int get_number_by_pos(FILE *f, size_t index, int *dig)
{
    fseek(f, index * sizeof(int), SEEK_SET);
    return read_from_file(f, dig);
}

void put_number_by_pos(FILE *f, size_t index, int dig)
{
    fseek(f, index * sizeof(int), SEEK_SET);
    fwrite(&dig, sizeof(int), 1, f);
}

