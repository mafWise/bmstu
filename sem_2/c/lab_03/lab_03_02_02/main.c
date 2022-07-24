#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

#define INPUT_ROWS_ERROR 73
#define INPUT_COLUMNS_ERROR 74
#define INPUT_MATRIX_ERROR 75

#define MAX_SIZE 10
#define SIZE_ARRAY 64

int is_digit_sum_odd(int el)
{
	int sum = 0;
	while (el)
	{
		sum += el % 10;
		el /= 10;
	}

	if (sum % 2 != 0)
		return EXIT_SUCCESS;

	return EXIT_FAILURE;
}

int arr_of_suitable_rows_id(int matrix[][SIZE_ARRAY], size_t rows, size_t columns, size_t arr_index[], size_t *arr_len)
{
	int el;
	int count;

	for (size_t i = rows - 1; i < rows; i--)
	{
		count = 0;
		
		for (size_t j = 0; j < columns; j++)
		{
			el = matrix[i][j];
			if (is_digit_sum_odd(el) == EXIT_SUCCESS)
				count++;
		}

		if (count >= 2)
		{
			arr_index[*arr_len] = i;
			(*arr_len)++;
		}
	}

	return EXIT_SUCCESS;
}

int matrix_input(int matrix[][SIZE_ARRAY], size_t rows, size_t columns)
{
	for (size_t i = 0; i < rows; i++)
		for (size_t j = 0; j < columns; j++)
			if (scanf("%d", &(matrix[i][j])) != 1)
				return EXIT_FAILURE;

	return EXIT_SUCCESS;
}

void matrix_output(int matrix[][SIZE_ARRAY], size_t rows, size_t columns)
{
	for (size_t i = 0; i < rows; i++)
	{
		for (size_t j = 0; j < columns; j++)
			printf("%d ", matrix[i][j]);
		printf("\n");
	}
}

void row_insert(int matrix[][SIZE_ARRAY], size_t *rows, size_t columns, size_t id)
{
	for (size_t i = *rows; i > id; i--)
		for (size_t j = 0; j < columns; j++)
			matrix[i][j] = matrix[i - 1][j];
			
	for (size_t j = 0; j < columns; j++)
		matrix[id][j] = -1;

	(*rows)++;
}

void rows_insert(int matrix[][SIZE_ARRAY], size_t *rows, size_t columns, size_t arr[], size_t arr_len)
{
	for (size_t i = 0; i < arr_len; i++)
		row_insert(matrix, rows, columns, arr[i]);
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

	size_t arr_len = 0;
	size_t arr[SIZE_ARRAY];
	
	arr_of_suitable_rows_id(matrix, rows, columns, arr, &arr_len);

	if (arr_len != 0)
		rows_insert(matrix, &rows, columns, arr, arr_len);

	matrix_output(matrix, rows, columns);
	
	return EXIT_SUCCESS;
}
