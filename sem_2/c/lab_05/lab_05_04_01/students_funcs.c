#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <inttypes.h>

#include "student.h"
#include "student_funcs.h"
#include "file_funcs.h"
#include "errors.h"

#include "students_funcs.h"

#define EPS 1e-6

int sort_students(FILE *f)
{
    size_t i = 0;
    student_t student1, student2;
    int tec;

    tec = get_student_by_pos(f, 0, &student1);
    
    while (tec == EXIT_SUCCESS && !feof(f))
    {
        if (i == 0 || strcmp(student1.surname, student2.surname) > 0)
        {
            student2 = student1;
            i++;
        }
        else if (strcmp(student1.surname, student2.surname) == 0)
        {
            if (strcmp(student1.name, student2.name) >= 0)
            {
                student2 = student1;
                i++;
            }
            else
            {
                swap_students(f, i, i - 1, &student1, &student2);
                get_student_by_pos(f, (--i) - 1, &student2);               
            }
        }
        else
        {
            swap_students(f, i, i - 1, &student1, &student2);
            get_student_by_pos(f, (--i) - 1, &student2);
        }

        tec = get_student_by_pos(f, i, &student1);
    }

    if (tec != EXIT_SUCCESS && feof(f))
        tec = EXIT_SUCCESS;

    return tec;
}

int average_all(FILE *f, double *average)
{
    student_t student;
    double sum = 0;
    int quantity = 0;
    int tec = read_student_from_file(f, &student);

    while (tec == EXIT_SUCCESS && !feof(f))
    {
        sum += student.grades[0];
        sum += student.grades[1];
        sum += student.grades[2];
        sum += student.grades[3];
        quantity += 4;

        tec = read_student_from_file(f, &student);
    }

    *average = sum / quantity;
    if (tec != EXIT_SUCCESS && feof(f))
        tec = EXIT_SUCCESS;

    fseek(f, 0, SEEK_SET);

    return tec;
}

int filter_students(FILE *f, size_t *size)
{
    size_t i = 0;
    student_t student1, student2;
    int tec;
    double average;
    double tmp1_local; 
    double tmp2_local;

    tec = average_all(f, &average);
    if (tec != EXIT_SUCCESS)
        return tec;

    tec = get_student_by_pos(f, 0, &student1);

    tmp1_local = average_local(student1);
    if (tmp1_local > average || fabs(tmp1_local - average) < EPS)
        (*size)++;

    while (tec == EXIT_SUCCESS && !feof(f))
    {      
        if (i == 0 || tmp1_local < average)
        {
            student2 = student1;
            tmp2_local = tmp1_local;
            i++;
        }
        else if (((tmp1_local > average || fabs(tmp1_local - average) < EPS) && tmp2_local < average))
        {
            swap_students(f, i, i - 1, &student1, &student2);
            if (i != 1)
                i--;
            else
                (*size)++;
            get_student_by_pos(f, i - 1, &student2);
            tmp2_local = average_local(student2);   
        }
        else
        {
            (*size)++;
            student2 = student1;
            tmp2_local = tmp1_local;
            i++;  
        }
        tec = get_student_by_pos(f, i, &student1);
        tmp1_local = average_local(student1);
    }
    if (tec != EXIT_SUCCESS && feof(f))
        tec = EXIT_SUCCESS;
        
    fseek(f, 0, SEEK_SET);

    return tec;
}

int print_students(FILE *f)
{
    student_t student;
    int tec = read_student_from_file(f, &student);

    while (tec == EXIT_SUCCESS && !feof(f))
    {
        // Т.к. feof возвращает отличное от нуля значение, 
        // если последняя файловая операция не была выполнена 
        // из-за достижения конца файла, то делаем доп проверку 
        if (!feof(f))
            print_student(student);

        tec = read_student_from_file(f, &student);
    }
    if (tec != EXIT_SUCCESS && feof(f))
        tec = EXIT_SUCCESS;

    return tec;
}

int find_and_write_students(FILE *f1, FILE *f2, char *substring)
{
    if (strlen(substring) > SURNAME_MAX)
        return SUBSTRING_LEN_ERROR;

    int check = 1;
    student_t student;
    int tec = read_student_from_file(f1, &student);
    
    while (tec == EXIT_SUCCESS && !feof(f1))
    {
        if (strstr(student.surname, substring) == student.surname)
        {
            check = 0;
            tec = write_student_into_file(f2, &student);
            if (tec != EXIT_SUCCESS)
                return tec;
        }
        tec = read_student_from_file(f1, &student);
    }
    
    if (tec != EXIT_SUCCESS && feof(f1))
        tec = EXIT_SUCCESS;
    if (check == 1)
        tec = WRITE_FILE_ERROR;

    return tec;
}

void swap_students(FILE *f, size_t index1, size_t index2, student_t *student1, student_t *student2)
{
    put_student_by_pos(f, index1, student2);
    put_student_by_pos(f, index2, student1);
}
