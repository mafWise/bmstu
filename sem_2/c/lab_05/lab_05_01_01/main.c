#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "process.h"

int main(void)
{	
	int fisrt_max, second_max;
	
	int tmp_exit_code = process(stdin, &fisrt_max, &second_max);
	if (tmp_exit_code != EXIT_SUCCESS)
		return tmp_exit_code;

	printf("%d %d", fisrt_max, second_max);

	return EXIT_SUCCESS;
}

