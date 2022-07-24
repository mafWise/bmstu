#include <stdio.h>
#include <stdlib.h>

#define INPUT_ROWS_ERROR 73
#define INPUT_COLUMNS_ERROR 74
#define INPUT_MATRIX_ERROR 75

#define MAX_SIZE 10
#define SIZE_ARRAY 64

void rows_swap(int row1[], int row2[], size_t columns)
{
	for (size_t i = 0; i < columns; i++)
	{
		int temp = row1[i];
		row1[i] = row2[i];
		row2[i] = temp;
	}
}

int elements_multiplication(int row[], size_t columns)
{
	int multiplication = 1;
	for (size_t i = 0; i < columns; i++)
		multiplication *= row[i];
	
	return multiplication;		
}

void matrix_bubble_sort(int matrix[][SIZE_ARRAY], size_t rows, size_t columns)
{
	for (size_t i = 0; i < rows; i++)
	{
		for (size_t j = 0; j < rows - 1; j++)
		{
			int m1 = elements_multiplication(matrix[j], columns);
			int m2 = elements_multiplication(matrix[j + 1], columns);
			if (m1 > m2)
				rows_swap(matrix[j], matrix[j + 1], columns);
		}
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

	matrix_bubble_sort(matrix, rows, columns);
	matrix_output(matrix, rows, columns);

	return EXIT_SUCCESS;
}
