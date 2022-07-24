#ifndef STUDENT
#define STUDENT

#include <stdint.h>

#define SURNAME_MAX 25
#define NAME_MAX 10
#define GRADES_QUANTITY 4

typedef struct
{
    char surname[SURNAME_MAX + 1];
    char name[NAME_MAX + 1];
    uint32_t grades[GRADES_QUANTITY];
} student_t;

#endif // #ifndef STUDENT