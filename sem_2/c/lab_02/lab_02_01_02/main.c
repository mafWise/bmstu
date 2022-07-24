#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define INPUT_LENGTH_ERROR 2
#define INPUT_ARRAY_ERROR 3
#define PROCESS_ERROR 4
#define SIZE_ARRAY 1024
#define MAX_SIZE 10
#define EPS 1e-6

int arr_input(int arr[], size_t len)
{
    for (size_t i = 0; i < len; i++)
        if (scanf("%d", (arr + i)) != 1)
            return EXIT_FAILURE;

    return EXIT_SUCCESS;
}

double negs_arithmetic_mean(int arr[], size_t len)
{
    int count = 0;
    double sum = 0.0;

    for (size_t i = 0; i < len; i++)
        if (*(arr + i) < 0)
        {
            count++;
            sum += *(arr + i);
        }

    if (count == 0)
        return 0.0;

    return sum / count;
}

int main(void)
{
    size_t len;

    if (scanf("%zu", &len) != 1 || len > MAX_SIZE || len <= 0)
    {
        printf("Error: wrong len of array");
        return INPUT_LENGTH_ERROR;
    }

    int arr[SIZE_ARRAY];

    if (arr_input(arr, len) == EXIT_FAILURE)
    {
        printf("Error: wrong element of array");
        return INPUT_ARRAY_ERROR;
    }

    double average = negs_arithmetic_mean(arr, len);

    if (fabs(average) < EPS)
    {
        printf("Error: there is no neg integers");
        return PROCESS_ERROR;
    }

    printf("%.6lf", average);

    return EXIT_SUCCESS;
}
