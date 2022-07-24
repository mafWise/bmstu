#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    double x1, y1;
    double x2, y2;
    double x3, y3;
    double p;
    double eps = 1e-6;

    printf("Enter the x1, y1, x2, y2, x3, y3: ");

    if (scanf("%lf", &x1) != 1)
        return EXIT_FAILURE;
    if (scanf("%lf", &y1) != 1)
        return EXIT_FAILURE;
    if (scanf("%lf", &x2) != 1)
        return EXIT_FAILURE;
    if (scanf("%lf", &y2) != 1)
        return EXIT_FAILURE;
    if (scanf("%lf", &x3) != 1)
        return EXIT_FAILURE;
    if (scanf("%lf", &y3) != 1)
        return EXIT_FAILURE;

    double s1 = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
    double s2 = sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3));
    double s3 = sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3));

    p = s1 + s2 + s3;

    if (fabs((x2 - x3) * (y1 - y2) - (y2 - y3) * (x1 - x3)) <= eps)
        p = 0;

    printf("Result: %.6lf\n", p);
    return EXIT_SUCCESS;
}
