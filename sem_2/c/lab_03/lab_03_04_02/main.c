#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define INPUT_ROWS_ERROR 73
#define INPUT_MATRIX_ERROR 75
#define INPUT_COLUMNS_ERROR 76

#define MAX_SIZE 10
#define SIZE_ARRAY 64

int find_max_suitable_int(int matrix[][SIZE_ARRAY], size_t size, int *max)
{
	int flag = 1;

	for (size_t i = 1; i < size; i++)
	{
		for (size_t j = size - 1; j >= size - i; j--)
		{
			//"Conditional jump or move depends on uninitialised value(s)"
			//Почему valgrind жалуется на это место при обратном порядке условий?
			//				🠓
			if ((flag == 1 || matrix[i][j] > *max) && abs(matrix[i][j]) % 10 == 5)
			{
				*max = matrix[i][j];
				flag = 0;
			}
		}
	}
	if (flag)
		return EXIT_FAILURE;
	
	return EXIT_SUCCESS;
}

int matrix_input(int matrix[][SIZE_ARRAY], size_t size)
{
	for (size_t i = 0; i < size; i++)
		for (size_t j = 0; j < size; j++)
			if (scanf("%d", &(matrix[i][j])) != 1)
				return EXIT_FAILURE;
	
	return EXIT_SUCCESS;
}

int main(void)
{
	size_t rows;
	size_t columns;

	if (scanf("%zu", &rows) != 1 || rows == 0 || rows > MAX_SIZE)
		return INPUT_ROWS_ERROR;
	if (scanf("%zu", &columns) != 1 || columns != rows)
		return INPUT_COLUMNS_ERROR;

	int matrix[SIZE_ARRAY][SIZE_ARRAY];

	if (matrix_input(matrix, columns) != EXIT_SUCCESS)
		return INPUT_MATRIX_ERROR;

	int max;

	if (find_max_suitable_int(matrix, columns, &max) != EXIT_SUCCESS)
		return EXIT_FAILURE;
	
	printf("%d", max);

	return EXIT_SUCCESS;
}
