/*
Л/р №5, задача №3
Целочисленны1 тип: int
Метод сортировки: гномья сортировка
"Направление" упорядочивания: по возрастанию
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "file_funcs.h"
#include "digs_funcs.h"
#include "get_put_funcs.h"

#define ARGS_ERROR 50

int main(int argc, char *argv[])
{	
	FILE *f;
	int tmp_exit_code;

	if (argc == 3)
	{
		tmp_exit_code = prev_check(argv[2]);
		
		if (tmp_exit_code != EXIT_SUCCESS)
			return tmp_exit_code;	
	}

	if (argc == 4 && strcmp(argv[1], "c") == 0)
	{
		f = fopen(argv[3], "wb");
		
		tmp_exit_code = fill_by_random_digs(f, argv[2]);

		fclose(f);
		return tmp_exit_code;
	}
	else if (argc == 3 && strcmp(argv[1], "p") == 0)
	{
		f = fopen(argv[2], "rb");

		tmp_exit_code = print_digs(f);

		fclose(f);
		return tmp_exit_code;
	}
	else if (argc == 3 && strcmp(argv[1], "s") == 0)
	{
		f = fopen(argv[2], "rb+");
		
		tmp_exit_code = sort_digs(f);

		fclose(f);
		return tmp_exit_code;		
	}

	return ARGS_ERROR;
}
