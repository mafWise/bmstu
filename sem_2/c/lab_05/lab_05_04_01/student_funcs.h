#ifndef STUDENT_FUNCS
#define STUDENT_FUNCS

void print_student(student_t student);

int get_student_by_pos(FILE *f, size_t index, student_t *student);

int put_student_by_pos(FILE *f, size_t index, student_t *student);

double average_local(student_t student);

#endif // #ifndef STUDENT_FUNCS