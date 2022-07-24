#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>


void print(uint32_t var)
{
    unsigned mask = 0x80000000;

    while (mask)
    {
        printf("%u", !!(var & mask));
        mask >>= 1;
    }
}

int main(void)
{
    uint32_t a;
    int n;
    printf("Enter the integer and number of postions: ");

    if (scanf("%" SCNu32, &a) != 1)
    {
        printf("Error:Incorrect input for the first variable\n");
        return EXIT_FAILURE;
    }
    if (scanf("%d", &n) != 1)
    {
        printf("Error:Incorrect input for the second variable\n");
        return EXIT_FAILURE;
    }
    if (n < 0)
    {
        printf("Error:Variable n must be positive\n");
        return EXIT_FAILURE;
    }

    a = (a << n) | (a >> (sizeof(uint32_t)*8 - n));
    printf("Result: ");
    print(a);

    return EXIT_SUCCESS;
}
