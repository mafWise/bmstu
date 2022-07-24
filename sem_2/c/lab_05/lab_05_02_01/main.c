#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "file_funcs.h"
#include "calc_funcs.h"

int main(int argc, char *args[])
{
	FILE *f;

	if (argc != 2)
		return EXIT_FAILURE;

	int tmp_exit_code = prev_check(args[1]);
	if (tmp_exit_code != EXIT_SUCCESS)
		return tmp_exit_code;

	int quantity = 0;
	double min = 0.0;
	double max = 0.0;

	f = fopen(args[1], "r");
	get_max_and_min(f, &max, &min);	
	fclose(f);

	f = fopen(args[1], "r");
	get_quantity(f, &quantity, max, min);	
	fclose(f);

	printf("%d", quantity);

	return EXIT_SUCCESS;
}
