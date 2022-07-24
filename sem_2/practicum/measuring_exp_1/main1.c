#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <time.h>
#include <sys/time.h>
#include <math.h>

#ifndef NMAX
#error Where is my NMAX, Lebowski?
#endif

typedef int array_t[NMAX];
array_t arr;
size_t len = NMAX;

int series_calculation(int arr[], size_t len)
{
    int sum = 0;
    int el = arr[0];
    size_t i = 0;
    
    while (i < len)
    {
        sum += el;
        if (el < 0)
            break;
        i++;
        el *= arr[i];
    }

    return sum;
}

int init(int arr[], size_t len)
{
    for (size_t i = 0; i < len; i++)
        arr[i] = i % 7;
    
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
    init(arr, len);
    
    int res;
    long long unsigned beg, end;

    beg = milliseconds_now();

    for(size_t i = 1; i < 1001; i++)
    {
        res = series_calculation(arr, len);
        arr[(len - 1) % i] = res;
    }
    
    end = milliseconds_now();

    arr[0] = arr[1];
    arr[1] = 1;

    printf("%llu\n", end - beg);

    return EXIT_SUCCESS;
}
