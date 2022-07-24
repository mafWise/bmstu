#include <stdio.h>
#include <stdlib.h>

#include "student.h"
#include "errors.h"

#include "file_funcs.h"

int prev_check(char *file_name)
{
	student_t student;
	
	FILE *f = fopen(file_name, "rb");
	int tec = EXIT_SUCCESS;

	if (f == NULL)
		return FILE_EXIST_ERROR;
	
	if (fread(&student, sizeof(student_t), 1, f) != 1)
		tec = CONTENT_VALIDITY_ERROR;

	fclose(f);
	return tec;
}

int read_student_from_file(FILE *f, student_t *student)
{
	if (fread(student, sizeof(student_t), 1, f) != 1)
		return CONTENT_VALIDITY_ERROR;
	
	return EXIT_SUCCESS;
}

int write_student_into_file(FILE *f, student_t *student)
{
	if (fwrite(student, sizeof(student_t), 1, f) != 1)
		return WRITE_FILE_ERROR;
	
	return EXIT_SUCCESS;
}
