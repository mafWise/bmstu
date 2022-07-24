#include <stdio.h>
#include <stdlib.h>

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

int is_square_number(int a)
{
    if (a < 0)
        return EXIT_FAILURE;

    int i = 1;
    while (a > 0)
    {
        a -= i;
        i += 2;
    }

    if (a != 0)
        return EXIT_FAILURE;

    return EXIT_SUCCESS;
}

void element_remove(int arr[], size_t len, size_t id)
{
    for (size_t j = id; j < len - 1; j++)
        *(arr + j) = *(arr + j + 1);
}

size_t find_and_remove(int arr[], size_t len)
{
    size_t i = 0;

    while (i < len)
    {
        if (is_square_number(arr[i]) == EXIT_SUCCESS)
        {
            element_remove(arr, len, i);
            len--;
        }
        else
            i++;
    }

    return len;
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

    if (arr_input(arr_in, len) == EXIT_FAILURE)
    {
        printf("Error: wrong element of array");
        return INPUT_ARRAY_ERROR;
    }

    len = find_and_remove(arr_in, len);
    if (len == 0)
        return PROCESS_ERROR;

    arr_print(arr_in, len);

    return EXIT_SUCCESS;
}
