#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

#include "student.h"
#include "file_funcs.h"

#include "student_funcs.h"

void print_student(student_t student)
{
    printf("%s ", student.surname);
    printf("%s ", student.name);
    printf("%" PRIu32 " ", student.grades[0]); 
    printf("%" PRIu32 " ", student.grades[1]);
    printf("%" PRIu32 " ", student.grades[2]);
    printf("%" PRIu32 "\n", student.grades[3]); 
}

int get_student_by_pos(FILE *f, size_t index, student_t *student)
{
    fseek(f, index * sizeof(student_t), SEEK_SET);
    return read_student_from_file(f, student);
}

int put_student_by_pos(FILE *f, size_t index, student_t *student)
{
    fseek(f, index * sizeof(student_t), SEEK_SET);
    return write_student_into_file(f, student);
}

double average_local(student_t student)
{
    return (double)(student.grades[0] + student.grades[1] + student.grades[2] + student.grades[3]) / 4;
}
