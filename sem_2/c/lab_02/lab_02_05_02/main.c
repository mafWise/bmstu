#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

#define INPUT_LENGTH_ERROR 2
#define INPUT_ARRAY_ERROR 3
#define SIZE_ARRAY 1024
#define MAX_SIZE 10

int arr_input(int *ps, int *pe)
{
    while (ps < pe)
    {
        if (scanf("%d", ps) != 1)
            return EXIT_FAILURE;
        ps++;
    }

    return EXIT_SUCCESS;
}

int series_calculation(int *ps, int *pe)
{
    int sum = 0;
    int el = *ps;

    while (ps < pe)
    {
        sum += el;
        if (el < 0)
            break;
        ps++;
        el *= *ps;
    }

    return sum;
}

int main(void)
{
    size_t len;

    if (scanf("%zu", &len) != 1 || len > MAX_SIZE || len == 0)
        return INPUT_LENGTH_ERROR;

    int arr[SIZE_ARRAY];

    if (arr_input(arr, arr + len) != EXIT_SUCCESS)
        return INPUT_ARRAY_ERROR;

    printf("%d", series_calculation(arr, arr + len));

    return EXIT_SUCCESS;
}
