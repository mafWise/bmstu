#ifndef FILE_FUNCS
#define FILE_FUNCS

int prev_check(char *file_name);

int write_student_into_file(FILE *f, student_t *student);

int read_student_from_file(FILE *f, student_t *student);

#endif // #ifndef FILE_FUNCS
