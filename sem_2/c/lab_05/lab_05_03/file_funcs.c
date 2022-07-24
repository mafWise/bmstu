#include <stdio.h>
#include <stdlib.h>

#define FILE_EXIST_ERROR 78
#define CONTENT_VALIDITY_ERROR 79

#include "file_funcs.h"

int prev_check(char *file_name)
{
	int dig_check;
	
	FILE *f = fopen(file_name, "rb");

	if (f == NULL)
		return FILE_EXIST_ERROR;

	if (fread(&dig_check, sizeof(int), 1, f) != 1)
		return CONTENT_VALIDITY_ERROR;

	fclose(f);
	return EXIT_SUCCESS;
}

int read_from_file(FILE *f, int *dig)
{
	if (fread(dig, sizeof(int), 1, f) != 1)
		return CONTENT_VALIDITY_ERROR;
	
	return EXIT_SUCCESS;
}
