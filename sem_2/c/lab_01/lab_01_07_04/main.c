#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double f(double x)
{
    return 1 / ((1 + x) * (1 + x) * (1 + x));
}

double s(double x, double e)
{
    double sum = 1;
    double s_el = 3 * -x;
    int i = 2;
    while (fabs(s_el) > e)
    {
        sum += s_el;
        s_el = s_el * (i + 2) * -x / i;
        i++;
    }
    return sum;
}


int main(void)
{
    double x;
    double e;

    printf("Enter the x value and the eps value: ");

    if (scanf("%lf", &x) != 1)
        return EXIT_FAILURE;
    if (scanf("%lf", &e) != 1)
        return EXIT_FAILURE;

    if (fabs(x) > 1)
        return EXIT_FAILURE;
    if (e <= 0 || e > 1)
        return EXIT_FAILURE;

    double s_sum = s(x, e);
    double f_el = f(x);
    double abs;
    double rel;


    abs = f_el - s_sum;
    rel = (f_el - s_sum) / f_el;

    if (abs < 0)
        abs *= -1.0;
    if (rel < 0)
        rel *= -1.0;

    printf("Result: %.6lf %.6lf %.6lf %.6lf\n", s_sum, f_el, abs, rel);
    return EXIT_SUCCESS;
}
