#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double g(double x, int key)
{
    return sqrt(key + x);
}

int main(void)
{
    double var;
    double s = 0.0;
    int n = 0;

    printf("Enter the integers: ");

    if (scanf("%lf", &var) != 1)
        return EXIT_FAILURE;

    while (var >= 0)
    {
        n += 1;
        s += g(var, n);
        if (scanf("%lf", &var) != 1)
            return EXIT_FAILURE;
    }

    if (n == 0)
        return EXIT_FAILURE;

    printf("Result: %.6lf\n", s / n);
    return EXIT_SUCCESS;
}
