#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

#include "student.h"

int main(void)
{

    char name[20] = "in.bin";

    FILE *f = fopen(name, "ab");

    int n;
    student_t student;

    scanf("%d", &n);

    if (n == -1)
    {
        
        scanf("\n%s", student.surname);
        scanf("\n%s", student.name);
        scanf("\n%" SCNu32, &student.grades[0]);
        scanf("\n%" SCNu32, &student.grades[1]);
        scanf("\n%" SCNu32, &student.grades[2]);
        scanf("\n%" SCNu32, &student.grades[3]);

        fseek(f, 0, SEEK_END);
        fwrite(&student, sizeof(student), 1, f);
    }    

    for (int i = 0; i < n; i++)
    {
        printf("%d", i);
        
        scanf("\n%s", student.surname);
        scanf("\n%s", student.name);
        scanf("\n%" SCNu32, &student.grades[0]);
        scanf("\n%" SCNu32, &student.grades[1]);
        scanf("\n%" SCNu32, &student.grades[2]);
        scanf("\n%" SCNu32, &student.grades[3]);

        fwrite(&student, sizeof(student), 1, f);
    }

    fclose(f);

    return 0;
}
