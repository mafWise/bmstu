#include <stdio.h>
#include <stdlib.h>

#define INPUT_ROWS_ERROR 73
#define INPUT_COLUMNS_ERROR 74

#define MAX_SIZE 10
#define SIZE_ARRAY 64

void bulls_move(int matrix[][SIZE_ARRAY], size_t rows, size_t columns)
{
	size_t i = 0;
	int counter = 0;


	while (i < columns)
	{
		for (size_t j = 0; j < rows; j++)
		{
			counter++;
			matrix[rows - j - 1][columns - i - 1] = counter;
		}
		i++;

		if (i >= columns)
			break;
		
		for (size_t j = 0; j < rows; j++)
		{
			counter++;
			matrix[j][columns - i - 1] = counter;
		}
		i++;
	}
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
	
	bulls_move(matrix, rows, columns);

	matrix_output(matrix, rows, columns);

	return EXIT_SUCCESS;
}
