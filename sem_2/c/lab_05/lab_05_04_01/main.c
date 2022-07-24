#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

#include "student.h"
#include "file_funcs.h"
#include "student_funcs.h"
#include "students_funcs.h"
#include "errors.h"

int main(int argc, char *argv[])
{
	FILE *f;
	FILE *f2;
	int tec; // tmp_exit_code

	if (argc < 3 || argc > 5)
		return ARGS_ERROR;
	
	if (strcmp(argv[1], "sb") == 0 && argc == 3)
	{
		tec = prev_check(argv[2]);
		if (tec != EXIT_SUCCESS)
			return tec;
		
		f = fopen(argv[2], "rb+");
		tec = sort_students(f);

		fclose(f);
		if (tec != EXIT_SUCCESS)
			return tec;

		f = fopen(argv[2], "rb");
		print_students(f);
		fclose(f);

		return tec;
	}
	else if (strcmp(argv[1], "fb") == 0 && argc == 5)
	{
		tec = prev_check(argv[2]);
		if (tec != EXIT_SUCCESS)
			return tec;		
		
		if (strcmp(argv[2], argv[3]) == 0 || strcmp(argv[4], "") == 0)
			return ARGS_ERROR;

		f = fopen(argv[2], "rb");
		f2 = fopen(argv[3], "wb");
		if (f2 == NULL)
		{
			fclose(f);
			return ARGS_ERROR;
		}

		tec = find_and_write_students(f, f2, argv[4]);

		fclose(f);
		fclose(f2);

		return tec;
	}
	else if (strcmp(argv[1], "db") == 0 && argc == 3)
	{
		tec = prev_check(argv[2]);
		if (tec != EXIT_SUCCESS)
			return tec;
	
		size_t size = 0;
		f = fopen(argv[2], "rb+");
		
		tec = filter_students(f, &size);
		if (tec == EXIT_SUCCESS)
			truncate(argv[2], size * sizeof(student_t));
		
		fclose(f);
		return tec;		
	}

	return ARGS_ERROR;
}