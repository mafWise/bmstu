#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    double r1, r2, r3;
    double r;
    double diviser;

    printf("Enter the first r, second r and third r: ");

    if (scanf("%lf", &r1) != 1)
        return EXIT_FAILURE;
    if (scanf("%lf", &r2) != 1)
        return EXIT_FAILURE;
    if (scanf("%lf", &r3) != 1)
        return EXIT_FAILURE;

    diviser = r1 * r2 + r2 * r3 + r3 * r1;
    r = r1 * r2 * r3 / (diviser);

    printf("Result: %.6lf\n", r);
    return EXIT_SUCCESS;
}
