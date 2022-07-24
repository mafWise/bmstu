#include <stdio.h>
#include <stdlib.h>

#include "file_funcs.h"
#include "get_put_funcs.h"
#include "digs_funcs.h"

#define WRITE_ERROR 20

int fill_by_random_digs(FILE *f, char *dig)
{
    int random_dig;
    int count;

    sscanf(dig, "%d", &count);

    for (int i = 0; i < count; i++)
    {
        random_dig = rand();
        if (fwrite(&random_dig, sizeof(int), 1, f) != 1)
            return WRITE_ERROR;
    }

    return EXIT_SUCCESS;
}

int print_digs(FILE *f)
{
    int dig;
    int tmp_exit_code = read_from_file(f, &dig);

    while (tmp_exit_code == EXIT_SUCCESS && !feof(f))
    { 
        // Т.к. feof возвращает отличное от нуля значение, 
        // если последняя файловая операция не была выполнена 
        // из-за достижения конца файла, то делаем доп проверку 
        if (!feof(f))
        {
            printf("%d\n", dig);
        }
        tmp_exit_code = read_from_file(f, &dig);
    }

    if (tmp_exit_code != EXIT_SUCCESS && feof(f))
        return EXIT_SUCCESS;

    return tmp_exit_code;
}


int sort_digs(FILE *f)
{
    size_t i = 0;
    int dig1, dig2;
    int tmp_exit_code;

    tmp_exit_code = get_number_by_pos(f, i, &dig1);

    while (tmp_exit_code == EXIT_SUCCESS && !feof(f))
    {
        if (i == 0 || dig1 >= dig2)
        {
            dig2 = dig1;
            i++;
        }
        else
        {
            swap(f, i, i - 1, dig1, dig2);
            i--;
            get_number_by_pos(f, i - 1, &dig2);
        }

        tmp_exit_code = get_number_by_pos(f, i, &dig1);
    }

    if (tmp_exit_code != EXIT_SUCCESS && feof(f))
    return EXIT_SUCCESS;

    return tmp_exit_code;
}

void swap(FILE *f, size_t index1, size_t index2, int dig1, int dig2)
{
    put_number_by_pos(f, index1, dig2);
    put_number_by_pos(f, index2, dig1);
}

