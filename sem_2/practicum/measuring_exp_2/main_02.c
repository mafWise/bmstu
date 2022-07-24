#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <time.h>
#include <sys/time.h>
#include <math.h>

#ifndef NMAX
#error Where is my NMAX, Lebowski?
#endif

typedef int matrix_t[NMAX][NMAX];
matrix_t matrix_a;
matrix_t matrix_b;
matrix_t matrix_c;
size_t len = NMAX;

int sum_of_matrix(int *matrix_a, int *matrix_b, int *matrix_c, size_t len)
{
    for (size_t i = 0; i < len; i++)
        for (size_t j = 0; j < len; j++)
                *(matrix_c + i * len + j) = *(matrix_a + i * len + j) * *(matrix_b + i * len + j);
    
    return EXIT_SUCCESS;
}

int init(int matrix[][NMAX], size_t len)
{
    for (size_t i = 0; i < len; i++)
        for (size_t j = 0; j < len; j++)
            matrix[i][j] = i % 7 + j;
    
    return EXIT_SUCCESS;
}

unsigned long long milliseconds_now(void)
{
    struct timeval val;
    if (gettimeofday(&val, NULL))
        return (unsigned long long) - 1;

    return val.tv_sec * 1000ULL + val.tv_usec / 1000ULL;
}

int main(void)
{
    init(matrix_a, len);
    init(matrix_b, len);
    init(matrix_c, len);
    
    int res;
    long long unsigned beg, end;

    beg = milliseconds_now();

    for(size_t i = 1; i < 1001; i++)
    {
        res = sum_of_matrix(*matrix_a, *matrix_b, *matrix_c, len);
        matrix_c[(len - 1) % i][(len - 1) % i] = res;
    }
    
    end = milliseconds_now();

    matrix_c[0][1] = matrix_c[1][0];
    matrix_c[1][0] = 1;

    printf("%llu\n", end - beg);

    return EXIT_SUCCESS;
}
