#include <stdio.h>
#include <stdlib.h>

#define INPUT_ROWS_ERROR 73
#define INPUT_COLUMNS_ERROR 74
#define INPUT_MATRIX_ERROR 75

#define MAX_SIZE 10
#define SIZE_ARRAY 64

void arr_of_suitable_columns(int matrix[][SIZE_ARRAY], size_t rows, size_t columns, int arr[])
{
	int a;
	int first;
	int second;

	

	for (size_t i = 0; i < columns; i++)
	{
		a = rows > 1 ? 1 : 0;
		second = matrix[0][i];
		for (size_t j = 0; j < rows - 1; j++)
		{
			first = matrix[j + 1][i];
			if ((first >= 0 && second >= 0) || (second <= 0 && first <= 0))
			{
				a = 0;
				break;
			}
			second = first;
		}
		arr[i] = a;
	}
}

int matrix_input(int matrix[][SIZE_ARRAY], size_t rows, size_t columns)
{
	for (size_t i = 0; i < rows; i++)
		for (size_t j = 0; j < columns; j++)
			if (scanf("%d", &(matrix[i][j])) != 1)
				return EXIT_FAILURE;
	
	return EXIT_SUCCESS;
}


void arr_print(int arr[], size_t len)
{
	for (size_t i = 0; i < len; i++)
	{
		printf("%d ", *(arr + i));
	}
	printf("\n");
}


int main(void)
{
	size_t rows, columns;

	if (scanf("%zu", &rows) != 1 || rows == 0 || rows > MAX_SIZE)
		return INPUT_ROWS_ERROR;
	if (scanf("%zu", &columns) != 1 || columns == 0 || columns > MAX_SIZE)
		return INPUT_COLUMNS_ERROR;

	int matrix[SIZE_ARRAY][SIZE_ARRAY];

	if (matrix_input(matrix, rows, columns) == EXIT_FAILURE)
		return INPUT_MATRIX_ERROR;

	int arr[SIZE_ARRAY];
	
	arr_of_suitable_columns(matrix, rows, columns, arr);
	arr_print(arr, columns);
	
	return EXIT_SUCCESS;
}
