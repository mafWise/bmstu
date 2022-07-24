#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define INPUT_LENGTH_ERROR 2
#define INPUT_ARRAY_ERROR 3
#define PROCESS_ERROR 4
#define SIZE_ARRAY 1024
#define MAX_SIZE 10

int arr_input(int arr[], size_t len)
{
    for (size_t i = 0; i < len; i++)
        if (scanf("%d", (arr + i)) != 1)
            return EXIT_FAILURE;

    return EXIT_SUCCESS;
}

void arr_print(int arr[], size_t len)
{
    for (size_t i = 0; i < len; i++)
        printf("%d ", *(arr + i));
}

void first_and_last(int el, int *first, int *last)
{
    *last = el % 10;

    //Отрезаем конец от числа, пока el не станет одной цифрой
    while (abs(el) > 9)
        el /= 10;
    *first = el % 10;
}

int copy_suitable_int(int arr_out[], int arr_in[], size_t *len)
{
    int el;
    size_t count = 0;
    int first, last;

    for (size_t i = 0; i < *len; i++)
    {
        el = arr_in[i];
        first_and_last(el, &first, &last);

        if (first == last)
        {
            arr_out[count] = arr_in[i];
            count++;
        }
    }

    if (len - count == len)
        return EXIT_FAILURE;

    *len = count;
    return EXIT_SUCCESS;
}

int main(void)
{
    size_t len;

    if (scanf("%zu", &len) != 1 || len > MAX_SIZE || len <= 0)
    {
        printf("Error: wrong length of array");
        return INPUT_LENGTH_ERROR;
    }

    int arr_in[SIZE_ARRAY];
    int arr_out[SIZE_ARRAY];

    if (arr_input(arr_in, len) == EXIT_FAILURE)
    {
        printf("Error: wrong element of array");
        return INPUT_ARRAY_ERROR;
    }

    if (copy_suitable_int(arr_out, arr_in, &len) == EXIT_FAILURE)
    {
        printf("Error: there is no suitable integer");
        return PROCESS_ERROR;
    }

    arr_print(arr_out, len);

    return EXIT_SUCCESS;
}
