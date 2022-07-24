#include <stdio.h>
#include <stdlib.h>

#include "file_funcs.h"

#define FILE_EXIST_ERROR 78
#define CONTENT_VALIDITY_ERROR 79

int prev_check(char name[])
{
	double check;
	int tec = EXIT_SUCCESS;

	FILE *f = fopen(name, "r");

	if (f == NULL)
		return FILE_EXIST_ERROR;
	if (fscanf(f, "%lf", &check) != 1)
		tec = CONTENT_VALIDITY_ERROR;

	fclose(f);
	return tec;
}
