#ifndef STUDENTS_FUNCS
#define STUDENTS_FUNCS

int sort_students(FILE *f);

void swap_students(FILE *f, size_t index1, size_t index2, student_t *student1, student_t *student2);

int average_all(FILE *f, double *average);

int filter_students(FILE *f, size_t *size);

int print_students(FILE *f);

int find_and_write_students(FILE *f1, FILE *f2, char *substring);

#endif // ifndef STUDENTS_FUNCS