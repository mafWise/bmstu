#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define INPUT_ROWS_ERROR 73
#define INPUT_COLUMNS_ERROR 74
#define INPUT_MATRIX_ERROR 75

#define MAX_SIZE 10
#define SIZE_ARRAY 64

void arr_reverse(int arr[], size_t arr_len)
{
	for (size_t i = 0; i < arr_len / 2; i++)
	{
		int temp = arr[i];
		arr[i] = arr[arr_len - i - 1];
		arr[arr_len - i - 1] = temp;
	}
}

int is_prime(int a)
{
	if (a <= 1)
		return EXIT_FAILURE;
	if (a % 2 == 0 && a != 2)
		return EXIT_FAILURE;

	for (int i = 3; i < a / 2 + 1; i += 2)
		if (a % i == 0)
			return EXIT_FAILURE;

	return EXIT_SUCCESS;
}

void replace_matrix_el_by_arr(int matrix[][SIZE_ARRAY], size_t rows, size_t columns, int arr[])
{
	size_t counter = 0;

	for (size_t i = 0; i < rows; i++)
		for (size_t j = 0; j < columns; j++)
			if (is_prime(matrix[i][j]) == EXIT_SUCCESS)
			{
				matrix[i][j] = arr[counter];
				counter++;
			}
}

void array_prime_int_fill(int matrix[][SIZE_ARRAY], size_t rows, size_t columns, int arr[], size_t *arr_len)
{
	for (size_t i = 0; i < rows; i++)
		for (size_t j = 0; j < columns; j++)
			if (is_prime(matrix[i][j]) == EXIT_SUCCESS)
			{
				arr[*arr_len] = matrix[i][j];
				(*arr_len)++;
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

void matrix_output(int matrix[][SIZE_ARRAY], size_t rows, size_t columns)
{
	for (size_t i = 0; i < rows; i++)
	{
		for (size_t j = 0; j < columns; j++)
			printf("%d ", matrix[i][j]);
		printf("\n");
	}
}

// void arr_print(int arr[], size_t len)
// {
//     for (size_t i = 0; i < len; i++)
// 	{
//         printf("\n%d ", *(arr + i));
// 	}
// 	printf("\n");
// }

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
	size_t arr_len = 0;

	array_prime_int_fill(matrix, rows, columns, arr, &arr_len);

	if (arr_len == 0)
		return INPUT_MATRIX_ERROR;

	arr_reverse(arr, arr_len);
	replace_matrix_el_by_arr(matrix, rows, columns, arr);
	
	matrix_output(matrix, rows, columns);
	
	return EXIT_SUCCESS;
}
