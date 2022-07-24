#include <stdio.h>
#include <stdlib.h>

#define INPUT_LENGTH_ERROR 2
#define SIZE_ARRAY 1024
#define MAX_SIZE 10

void insertion_sort(int arr[], size_t len)
{
    int el;
    size_t id;

    for (size_t i = 1; i < len; i++)
    {
        el = *(arr + i);
        id = i - 1;

        while (id < len && *(arr + id) > el)
        {
            *(arr + id + 1) = *(arr + id);
            id--;
        }

        *(arr + id + 1) = el;
    }
}

size_t arr_input(int arr[])
{
    size_t i;
    for (i = 0; i < MAX_SIZE + 1; i++)
        if (scanf("%d", (arr + i)) != 1)
            break;
    return i;
}

void arr_print(int arr[], size_t len)
{
    for (size_t i = 0; i < len; i++)
        printf("%d ", *(arr + i));
}

int main(void)
{
    size_t len;
    int arr[SIZE_ARRAY];
    int exit_code = 0;

    len = arr_input(arr);

    if (len >= MAX_SIZE + 1)
    {
        len = 10;
        exit_code = 100;
    }
    else if (len == 0)
        return INPUT_LENGTH_ERROR;

    insertion_sort(arr, len);
    arr_print(arr, len);

    return exit_code;
}
